import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

linear_data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
exponential_data = linear_data ** 2

plt.figure()
# plot the linear data and the exponential data
plt.plot(linear_data, '-o', exponential_data, '-o')
plt.plot([22, 44, 55], '--r')
plt.xlabel('Some data')
plt.ylabel('Some other data')
plt.title('A title')
plt.legend(['Baseline', 'Competition', 'Us'])
plt.gca().fill_between(range(len(exponential_data)),
                       linear_data, exponential_data,
                       facecolor='blue',
                       alpha=0.35)
plt.show()

# Complete Example
# TODO -- Fix Bug (matplotlib does not support generators as input)
# plt.figure()
# observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
# plt.plot(observation_dates, linear_data, '-o', observation_dates, exponential_data, '-o')
# plt.figure()
# observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
# observation_dates = map(pd.to_datetime, observation_dates)  # trying to plot a map will result in an error
# plt.plot(observation_dates, linear_data, '-o', observation_dates, exponential_data, '-o')
# plt.figure()
# observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
# observation_dates = list(map(pd.to_datetime, observation_dates))  # convert the map to a list to get rid of the error
# plt.plot(observation_dates, linear_data, '-o', observation_dates, exponential_data, '-o')
# x = plt.gca().xaxis
#
# for item in x.get_ticklabels():
#     item.set_rotation(45)
# plt.subplots_adjust(bottom=0.25)
# ax = plt.gca()
# ax.set_xlabel('Date')
# ax.set_ylabel('Units')
# ax.set_title('Exponential vs. Linear performance')
# ax.set_title("Exponential ($x^2$) vs. Linear ($x$) performance")
