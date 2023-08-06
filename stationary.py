# assume that the data is stationary

'''
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("AirPassengers.csv",	header=0, index_col=0)

print(data.head(10))

plt.plot(data)
plt.show()
'''

# different groups and calculate the mean and variance of different groups and check for consistency

import pandas as pd
data = pd.read_csv("AirPassengers.csv", header=0, index_col=0)
values = data.values
parts = int(len(values)/3)
part_1, part_2, part_3 = values[0:parts], values[parts:(parts*2)], values[(parts*2):(parts*3)]
mean_1, mean_2, mean_3 = part_1.mean(), part_2.mean(), part_3.mean()

var_1, var_2, var_3 = part_1.var(), part_2.var(), part_3.var()
print('mean1=%f, mean2=%f, mean2=%f' % (mean_1, mean_2, mean_3))
print('variance1=%f, variance2=%f, variance2=%f' % (var_1, var_2, var_3))
