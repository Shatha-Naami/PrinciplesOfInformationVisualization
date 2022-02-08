import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.ticker as ticker

# STEP 1
df = pd.read_csv('data_temperatures_nola.csv')

# STEP 2
df.loc[:, 'Data_Value'] *= 0.1  # convert to degree celsius
df['Date'] = pd.to_datetime(df['Date'])  # Changing the dtype of the date to pandas datetime

# day of the year
df['Day'] = pd.DatetimeIndex(df['Date']).day
df['Month'] = pd.DatetimeIndex(df['Date']).month
df = df.set_index(['Month', 'Day'])
df.sort_index(inplace=True)

# Discarding all the entries for 29th Feb of any year; only 365 days of the year are considered
selected_df = df.loc[2, 29]
df = df[~df.index.isin(selected_df.index)]
print(df.head(5))

# STEP 3
df['Year'] = pd.DatetimeIndex(df['Date']).year
df_2015 = df[df['Year'] == 2015]
df = df[df['Year'] != 2015]

max_temp_df = df[df['Element'] == 'TMAX']
min_temp_df = df[df['Element'] == 'TMIN']

max_temp = max_temp_df.groupby(level=['Month', 'Day'])['Data_Value'].max()
min_temp = min_temp_df.groupby(level=['Month', 'Day'])['Data_Value'].min()

max_temp_df_2015 = df_2015[df_2015['Element'] == 'TMAX']
min_temp_df_2015 = df_2015[df_2015['Element'] == 'TMIN']

max_temp_df_2015 = max_temp_df_2015.groupby(level=['Month', 'Day']).max()[['Data_Value', 'Date']]
min_temp_df_2015 = min_temp_df_2015.groupby(level=['Month', 'Day']).min()[['Data_Value', 'Date']]

# STEP 4
date_range = df_2015['Date'].unique()

# Creating figure and an axis
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))
ax.set_title('Ten Year Record (2005-2014) Was Broken in 2015')  # Setting the title
ax.yaxis.grid()

plt.plot(date_range, max_temp.values, '#FF9100', linewidth=1, alpha=0.75, label='2005-2014 Highs')
plt.plot(date_range, min_temp.values, '#80D8FF', linewidth=1, alpha=0.75, label='2005-2014 Lows')
plt.fill_between(date_range, min_temp, max_temp, facecolor='#EEEEEE')
plt.legend(loc=1).get_frame().set_edgecolor('white')
my_label_max = "2015 Highs"
my_label_min = "2015 Lows"
for idx, rows in max_temp_df_2015.iterrows():
    if rows['Data_Value'] > max_temp.loc[idx]:
        plt.scatter(rows['Date'], rows['Data_Value'], c='#E65100', marker='.', label=my_label_max)
        my_label_max = "_nolegend_"  # To avoid duplicate labels in the legend
for idx, rows in min_temp_df_2015.iterrows():
    if rows['Data_Value'] < min_temp.loc[idx]:
        plt.scatter(rows['Date'], rows['Data_Value'], c='#0091EA', marker='.', label=my_label_min)
        my_label_min = "_nolegend_"

ax.legend(loc=1).get_frame().set_edgecolor('white')
xmin, xmax = date_range[0], date_range[-1]
ax.set_xlim(xmin, xmax)

ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=15))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))

xticks = ax.xaxis.get_minor_ticks()
for xtick in xticks:
    xtick.tick1line.set_markersize(0)
    xtick.tick2line.set_markersize(0)
    xtick.label1.set_horizontalalignment('center')
ax.set_ylabel('Temperatures $(^{\circ}$C)')

ymin, ymax = -10, 50
ax.set_ylim(ymin, ymax)

yticks = ax.yaxis.get_major_ticks()
yticks[0].label1.set_visible(False)
yticks[1].label1.set_visible(False)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2 = ax.twinx()
ax2.set_ylabel('Temperatures $(^{\circ}$F)')


def C_to_F(temp_c):  # Celsius to Fahrenheit
    return 9 / 5 * temp_c + 32


ax2.set_ylim(C_to_F(ymin), C_to_F(ymax))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))

fig.tight_layout()
plt.show()
