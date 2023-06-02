# This chapter focuses on handing and manipulating Date, Time, and Time Series Data

# Code is not mine
    # All code comes from Packt and the author is Pushpak Dagade
    

import pandas as pd 
import numpy as np

# Time series data is a series of data consisting of equally spaced timestamps and multiple
# points of data descibing trading in that particular time frame (or in the context of 
# the financial crash modeling, a time series describing composite s&p 500 index prices over 120 years)

from datetime import datetime
from datetime import timedelta

# dt1 = datetime.now()
# print(f'Approach #1: {dt1}')

# attributes related to date and time

# year, month, day, hour, minute, second, microsecond (10^-9?), tzinfo (Timezone)

# can use date() and time() to extract date and time information

# timedelta class

td1 = timedelta(days=5)
print(f'Time Difference: {td1}')

td2 = timedelta(days=4)
print(f'Time difference: {td2}')


# skipped ahead a bit to dataframes

# this is meant to in interpreter so it won't run standalone unless i change .datetime to something else
time_series_data = [{'date': datetime(2019, 11, 13, 9, 0),
 'open': 71.8075, 'high': 71.845, 'low': 71.7775,
 'close': 71.7925, 'volume': 219512},
{'date': datetime(2019, 11, 13, 9, 15),
 'open': 71.7925, 'high': 71.8, 'low': 71.78,
 'close': 71.7925, 'volume': 59252},
{'date': datetime(2019, 11, 13, 9, 30),
 'open': 71.7925, 'high': 71.8125, 'low': 71.76,
 'close': 71.7625, 'volume': 57187},
{'date': datetime(2019, 11, 13, 9, 45), 
'open': 71.76, 'high': 71.765, 'low': 71.735,
 'close': 71.7425, 'volume': 43048},
{'date': datetime(2019, 11, 13, 10, 0),
 'open': 71.7425, 'high': 71.78, 'low': 71.7425,
 'close': 71.7775, 'volume': 45863},
{'date': datetime(2019, 11, 13, 10, 15),
 'open': 71.775, 'high': 71.8225, 'low': 71.77,
 'close': 71.815, 'volume': 42460},
{'date': datetime(2019, 11, 13, 10, 30),
 'open': 71.815, 'high': 71.83, 'low': 71.7775,
 'close': 71.78, 'volume': 62403},
{'date': datetime(2019, 11, 13, 10, 45),
 'open': 71.775, 'high': 71.7875, 'low': 71.7475,
 'close': 71.7525, 'volume': 34090},
{'date': datetime(2019, 11, 13, 11, 0),
 'open': 71.7525, 'high': 71.7825, 'low': 71.7475,
 'close': 71.7625, 'volume': 39320},
{'date': datetime(2019, 11, 13, 11, 15),
 'open': 71.7625, 'high': 71.7925, 'low': 71.76,
 'close': 71.7875, 'volume': 20190}]

df_ex = pd.DataFrame(time_series_data)

# different ways to gather information and also to specify columns of a df
print(df_ex.head())
print(df_ex.columns.tolist())
print(pd.DataFrame(time_series_data, 
                   columns=['close','date', 'open', 'high', 'low', 'volume']))

# custom index
print(pd.DataFrame(time_series_data, index=range(10, 20)))

# df manipulation reminders and practice

