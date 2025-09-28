import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def draw_cat_plot():
    # 1) Import data
    df = pd.read_csv(r'D:\DataAnalystSolution\assets\data\medical_examination.csv', na_values=' ?')

    # 2) Add 'overweight' column
    # BMI = weight (kg) / (height (m))^2 ; overweight when BMI > 25
    bmi = df['weight'] / ((df['height'] / 100) ** 2)
    df['overweight'] = (bmi > 25).astype(int)

    # 3) Normalize data: 0 is good, 1 is bad for 'cholesterol' and 'gluc'
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)

    # 4) Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 5) Group and reformat the data to show counts of each feature split by cardio
    # We will not aggregate counts here because seaborn.catplot(kind='count') will count for us.
    # But for explicit counts (optional) you could group. The tests expect the melted df shape etc.
    # 6) Draw the catplot
    catplot = sns.catplot(
        data=df_cat,
        kind='count',
        x='variable',
        hue='value',
        col='cardio'
    )

    fig = catplot.fig
    # Do not modify the next two lines (FCC requirement)
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # 1) Import data
    df = pd.read_csv(r'D:\DataAnalystSolution\assets\data\medical_examination.csv')

    # 2) Add 'overweight' column
    bmi = df['weight'] / ((df['height'] / 100) ** 2)
    df['overweight'] = (bmi > 25).astype(int)

    # 3) Normalize 'cholesterol' and 'gluc' (0 = good, 1 = bad)
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)

    # 4) Clean the data:
    # - Keep rows where ap_lo <= ap_hi
    # - Remove height outliers (keep between 2.5th and 97.5th percentiles)
    # - Remove weight outliers (keep between 2.5th and 97.5th percentiles)
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ].copy()

    # 5) Calculate the correlation matrix
    corr = df_heat.corr()

    # 6) Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 7) Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 8) Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        vmax=0.3,
        vmin=-0.1,
        linewidths=0.5,
        square=True,
        cbar_kws={'shrink': 0.5}
    )

    # Do not modify the next two lines (FCC requirement)
    fig.savefig('heatmap.png')
    return fig
