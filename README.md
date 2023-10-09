# Simple-Linear-Regression

Linear regressions are statistical tools to calculate the relationship between two or more variables.
What we want is to know how an independent variable (X) or several independent variables (X_i) influence the dependent variable (Y).
A linear regression line has an equation of the form Y = a + b * X + e_i, where X is the explanatory variable and Y is the dependent variable. e_i is the erroor term. The slope of the line is b, and a is the intercept (the value of y when x = 0).
The most common method for fitting a regression line is the Ordinary Least Ssquares(OLS). OLS minimizes the sum of the squares of the vertical deviations from each data point to the line. Because the deviations are first squared, then summed, there are no cancellations between positive and negative values.
Some assumptions need to be considered for this to work. The most important ones  are: the conditional mean should be zero, there is no multi-collinearity (or perfect collinearity), random sampling of observations, there is homoscedasticity (the error terms in the regression should all have a constant variance) and no autocorrelation.
AS an example of how OLS works a data set of cars sold in the US in 1978 of price versus weight accounting for the 74 observations will be used. We can notice a positive relationship between the weight and the price of the cars so we can hypothesize that the heavier a car is, the more expensive it will be but several problems like ommited variable bias can be present and we have to consider them when using OLS.
