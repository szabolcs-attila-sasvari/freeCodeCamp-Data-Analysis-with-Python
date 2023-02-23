import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975)) & (df['value'].quantile(0.025) <= df['value'])]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(18, 6))
    ax = plt.plot(df.index, df['value'], 'r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.insert(0, 'year', df_bar.index.year)
    df_bar.insert(1, 'month', df_bar.index.month)
    df_bar.reset_index(inplace=True)
    df_bar.drop(['date'], axis=1, inplace=True)
    df_bar = df_bar.groupby(['year', 'month'], as_index=False).sum()
    df_bar['month'] = pd.to_datetime(df_bar['month'], format='%m').dt.month_name()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.barplot(data=df_bar, x='year', y='value', hue='month', palette=sns.color_palette())

    handles, labels = plt.gca().get_legend_handles_labels()
    legend_order = [8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7]
    plt.legend(title='Months', loc='upper left', handles=[handles[order] for order in legend_order],
               labels=[labels[order] for order in legend_order])

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.xticks(rotation=90)
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    print(df_box['month'])

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))
    sns.boxplot(x=df_box['year'], y=df_box['value'], ax=ax[0])
    ax[0].set(title='Year-wise Box Plot (Trend)')
    ax[0].set(xlabel='Year')
    ax[0].set(ylabel='Page Views')
    sns.boxplot(x=df_box['month'], y=df_box['value'], ax=ax[1],
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', ])
    ax[1].set(title='Month-wise Box Plot (Seasonality)')
    ax[1].set(xlabel='Month')
    ax[1].set(ylabel='Page Views')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
