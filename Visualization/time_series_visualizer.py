import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

# Import data
df = pd.read_csv(r'D:\DataAnalystSolution\assets\data\fcc-forum-pageviews.csv', 
                 parse_dates=['date'], 
                 index_col='date')

# Clean data by removing top 2.5% and bottom 2.5% of page views
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Make a copy of cleaned data
    fig, ax = plt.subplots(figsize=(15,5))
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Prepare data for bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Group by year and month and calculate average page views
    df_bar_grouped = df_bar.groupby(['year','month'])['value'].mean().unstack()

    # Plot
    fig = df_bar_grouped.plot(kind='bar', figsize=(12,8)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend([calendar.month_name[m] for m in range(1,13)], title="Months")
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.month
    df_box['month_name'] = df_box['date'].dt.strftime('%b')

    # Order of months for box plot
    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    fig, axes = plt.subplots(1, 2, figsize=(20,7))

    # Year-wise box plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot (Seasonality)
    sns.boxplot(x='month_name', y='value', data=df_box, ax=axes[1], order=month_order)
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig
