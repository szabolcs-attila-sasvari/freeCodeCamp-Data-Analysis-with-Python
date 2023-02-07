<h1 align="center"><string>Sea Level Predictor</string></h1>

## **Assignment**

You will analyze a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.

Use the data to complete the following tasks:

- Use Pandas to import the data from <code>epa-sea-level.csv</code>.
- Use matplotlib to create a scatter plot using the <code>Year</code> column as the x-axis and the <code>CSIRO Adjusted Sea Level</code> column as the y-axis.
- Use the <code>linregress</code> function from <code>scipy.stats</code> to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
- Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
- The x label should be <code>Year</code>, the y label should be <code>Sea Level (inches)</code>, and the title should be <code>Rise in Sea Level</code>.

Unit tests are written for you under <code>test_module.py</code>.

The boilerplate also includes commands to save and return the image.

Development

For development, you can use <code>main.py</code> to test your functions. Click the "run" button and <code>main.py</code> will run.

Testing

We imported the tests from <code>test_module.py</code> to <code>main.py</code> for your convenience. The tests will run automatically whenever you hit the "run" button.

Submitting

Copy your project's URL and submit it to freeCodeCamp.

Data Source

<ins>Global Average Absolute Sea Level Change</ins>, 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.
