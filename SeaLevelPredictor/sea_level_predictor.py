import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv(r'D:\DataAnalystSolution\assets\data\epa-sea-level.csv', na_values=' ?')

    # Create scatter plot
    plt.figure(figsize=(12,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10)

    # Create first line of best fit (1880–2050)
    slope1, intercept1, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = list(range(1880, 2051))
    line1 = [slope1*x + intercept1 for x in years_extended]
    plt.plot(years_extended, line1, color='red', label='Fit 1880–2050')

    # Create second line of best fit (2000–2050)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    line2 = [slope2*x + intercept2 for x in years_extended]
    plt.plot(years_extended, line2, color='green', label='Fit 2000–2050')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save figure
    plt.savefig('sea_level_plot.png')
    return plt.gcf()
