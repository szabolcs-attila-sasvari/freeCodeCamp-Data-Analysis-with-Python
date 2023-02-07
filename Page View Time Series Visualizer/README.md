<h1 align="center"><string>Page View Time Series Visualizer
</string></h1>

## **Assignment**

For this project you will visualize time series data using a line chart, bar chart, and box plots. You will use Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations will help you understand the patterns in visits and identify yearly and monthly growth.

Use the data to complete the following tasks:

- Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the <code>date</code> column.
- Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
- Create a <code>draw_line_plot</code> function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be <code>Daily freeCodeCamp Forum Page Views 5/2016-12/2019</code>. The label on the x axis should be <code>Date</code> and the label on the y axis should be <code>Page Views</code>.
- Create a <code>draw_bar_plot</code> function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of <code>Months</code>. On the chart, the label on the x axis should be <code>Years</code> and the label on the y axis should be <code>Average Page Views</code>.
- Create a <code>draw_box_plot</code> function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be <code>Year-wise Box Plot (Trend)</code> and the title of the second chart should be <code>Month-wise Box Plot (Seasonality)</code>. Make sure the month labels on bottom start at <code>Jan</code> and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.

For each chart, make sure to use a copy of the data frame. Unit tests are written for you under <code>test_module.py</code>.

The boilerplate also includes commands to save and return the image.

## **Development**

For development, you can use <code>main.py</code> to test your functions. Click the "run" button and <code>main.py</code> will run.

## **Testing**

We imported the tests from <code>test_module.py</code> to <code>main.py</code> for your convenience. The tests will run automatically whenever you hit the "run" button.

## **Submitting**

Copy your project's URL and submit it to freeCodeCamp.
