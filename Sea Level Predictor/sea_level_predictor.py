import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')
    ticks = np.arange(1850, 2100, 25)
    plt.xticks(ticks)

    # Create first line of best fit
    first_extended = np.arange(df['Year'].iloc[0], 2051, 1)
    first_reg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(first_extended, [first_reg.intercept + first_reg.slope * x for x in first_extended], 'r')

    # Create second line of best fit
    second_extended = np.arange(2000, 2051, 1)
    twentieth_century = df[2000 <= df['Year']]
    second_reg = linregress(twentieth_century['Year'], twentieth_century['CSIRO Adjusted Sea Level'])
    plt.plot(second_extended, [second_reg.intercept + second_reg.slope * x for x in second_extended], 'g')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
