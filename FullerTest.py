# Ho (Null Hypothesis): The time series data is non-stationary
# H1 (alternate Hypothesis): The time series data is stationary

#  The test results are interpreted with a p-value if p > 0.05 fails to reject the null hypothesis, else if p <= 0.05 reject the null hypothesis.

import pandas as pd
from statsmodels.tsa.stattools import adfuller

data = pd.read_csv("AirPassengers.csv", header=0, index_col=0)
values = data.values
res = adfuller(values)

print('Augmneted Dickey_fuller Statistic: %f' % res[0])
print('p-value: %f' % res[1])

print('critical values at different levels:')
for k, v in res[4].items():	print('\t%s: %.3f' % (k, v))
