
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

data = pd.read_stata("/Users/martinfranco/Desktop/Universität/Mikroökonomik/Applied Microeconometrics/Exercises/dta/auto.dta")
data.to_csv("/Users/martinfranco/Desktop/Universität/Mikroökonomik/Applied Microeconometrics/Exercises/dta/auto.dta")
print(data)



x = data["weight"]
y = data["price"]

#### Plot the scatter plot with weight and price

plt.scatter(x, y)
plt.title("Price on weight")
plt.xlabel("weight")
plt.ylabel("price")
plt.show()

#### Run a regression of price on weight.

x = sm.add_constant(x)
model_1 = sm.OLS(y,x)
results_1 = model_1.fit()
print(results_1.summary())

#### Another way of coding the same regression

model_2 = sm.OLS(data.price, sm.add_constant(data.weight))
results_2 = model_2.fit()
print(results_2.summary())

#### Another way of coding the same regression(this time like in R).

model_3 = sm.OLS.from_formula("price ~ 1 + weight", data = data)
results_3 = model_3.fit()
print(results_3.summary())

#### coefficient = 2.044
#### we end up with this equation: y = -6.707 + 2.044 * weight + e_i

#### Plot the regression line

sns.regplot(x = "weight", y = "price", data = data, ci = None).set(title = "Weight on Price")
plt.show()

#### The regressor weihgt is statistically significant but the R^2 is 0.29, so the regression does not explain that much of the sample variance of the independent variable.
#### The price of a car can be influenced by several different factors that are not being considered in the regression which allows us to say that Omitted Variable Bias (OVB) is present.


#### Predicted price of a car weighing 2,500lb.

weight2500 = (1,2500)
results_1.predict(weight2500)

#### Predicted price of a car weighting 2500lb is 5103.449.


#### Predicted price of a car weighing 1,400lb.
weight4000 = (1,4000)
results_1.predict(weight4000)
#### Predicted price of a car weighting 4000lb is 8169.54.



#### Expected price difference between two cars, one of which is 500lb heavier.


differenceinweight500 = (0,500)
results_1.predict(differenceinweight500)

#### The difference in the expected price of two cars, one on which is heavier of 500lb, is given by Yi+500-Yi=( -6.707 + 2.044*(xi+500) +ei)-( -6.707 + 2.044*xi +ei)= 2.044*500= 1022.031.


#### Predicted price of a car weighing 500lb.

weight500 = (1,500)
results_1.predict(weight500)
min(data["weight"])

#### The predicted price of a car weighing 500 lb is 1015.32. This price does not make much sense since the minimum weight observed in the sample is 1760.











































































































