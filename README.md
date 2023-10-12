# Does the weight of a car affect its price? Simple Linear Regression

To see if the weight of a car affects its price I used simple linear regression with a data set of cars sold in the US in 1978 accounting for the 74 observations of price versus weight. We can notice a positive relationship between the weight and the price of the cars so we can hypothesize that the heavier a car is, the more expensive it will be. As an argument for this is that the more pieces the car has inside equals a more weight and the more pieces it has the more it will cost.

Linear regressions are statistical tools to calculate the relationship between two or more variables.
What we want is to know how an independent variable or several independent variables (X) influence the dependent variable (Y).

A linear regression line has an equation of the form Y = a + b * X + e_i, where X is the explanatory variable and Y is the dependent variable. e_i is the erroor term. The slope of the line is b, and a is the intercept (the value of y when x = 0).
The most common method for fitting a regression line is the Ordinary Least Ssquares(OLS). OLS minimizes the sum of the squares of the vertical deviations from each data point to the line. Because the deviations are first squared, then summed, there are no cancellations between positive and negative values.

Some assumptions need to be considered for this to work. The most important ones  are: the conditional mean should be zero, there is no multi-collinearity (or perfect collinearity), random sampling of observations, there is homoscedasticity (the error terms in the regression should all have a constant variance) and no autocorrelation.
Also, several problems like ommited variable bias can be present and we have to consider them when using OLS. For example in this case we can think that the brand and its exposition plays a role in the price of the car as well as the quality of the pieces inside it. All this can affect directly the price of the car and omitting those variables might affect the calculation of our already cconsidered variable.
