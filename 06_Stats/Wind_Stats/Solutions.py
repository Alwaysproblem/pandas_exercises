#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '06_Stats\Wind_Stats'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Wind Statistics
#%% [markdown]
# ### Introduction:
# 
# The data have been modified to contain some missing values, identified by NaN.  
# Using pandas should make this exercise
# easier, in particular for the bonus question.
# 
# You should be able to perform all of these operations without using
# a for loop or other looping construct.
# 
# 
# 1. The data in 'wind.data' has the following format:

#%%
"""
Yr Mo Dy   RPT   VAL   ROS   KIL   SHA   BIR   DUB   CLA   MUL   CLO   BEL   MAL
61  1  1 15.04 14.96 13.17  9.29   NaN  9.87 13.67 10.25 10.83 12.58 18.50 15.04
61  1  2 14.71   NaN 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25   NaN  8.50  7.67 12.75 12.71
"""

#%% [markdown]
#    The first three columns are year, month and day.  The
#    remaining 12 columns are average windspeeds in knots at 12
#    locations in Ireland on that day.   
# 
#    More information about the dataset go [here](wind.desc).
#%% [markdown]
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd
import datetime

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://github.com/guipsamora/pandas_exercises/blob/master/06_Stats/Wind_Stats/wind.data)
#%% [markdown]
# ### Step 3. Assign it to a variable called data and replace the first 3 columns by a proper datetime index.

#%%
# parse_dates gets 0, 1, 2 columns and parses them as the index
data_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'
data = pd.read_csv(data_url, sep = r"\s+", parse_dates = [[0,1,2]], infer_datetime_format=True)
data.head()

# OR



#%% [markdown]
# ### Step 4. Year 2061? Do we really have data from this year? Create a function to fix it and apply it.

#%%
# The problem is that the dates are 2061 and so on...

# function that uses datetime
def fix_century(x):
  year = x.year - 100 if x.year > 1989 else x.year
  return datetime.date(year, x.month, x.day)

# apply the function fix_century on the column and replace the values to the right ones
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)

# data.info()
data.head()

#%% [markdown]
# ### Step 5. Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns].

#%%
# transform Yr_Mo_Dy it to date type datetime64
data["Yr_Mo_Dy"] = pd.to_datetime(data["Yr_Mo_Dy"])

# set 'Yr_Mo_Dy' as the index
data = data.set_index('Yr_Mo_Dy')

data.head()
# data.info()

#%% [markdown]
# ### Step 6. Compute how many values are missing for each location over the entire record.  
# #### They should be ignored in all calculations below. 

#%%
# "Number of non-missing values for each location: "
data.isnull().sum()

#%% [markdown]
# ### Step 7. Compute how many non-missing values there are in total.

#%%
# number of columns minus the number of missing values for each location
data.shape[0] - data.isnull().sum()

# OR

data.notnull().sum()

#%% [markdown]
# ### Step 8. Calculate the mean windspeeds of the windspeeds over all the locations and all the times.
# #### A single number for the entire dataset.

#%%
data.fillna(0).values.flatten().mean()

#%% [markdown]
# ### Step 9. Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days 
# 
# #### A different set of numbers for each location.

#%%
data.describe(percentiles=[])

#%% [markdown]
# ### Step 10. Create a DataFrame called day_stats and calculate the min, max and mean windspeed and standard deviations of the windspeeds across all the locations at each day.
# 
# #### A different set of numbers for each day.

#%%
# create the dataframe
day_stats = pd.DataFrame()

# this time we determine axis equals to one so it gets each row.
day_stats['min'] = data.min(axis = 1) # min
day_stats['max'] = data.max(axis = 1) # max 
day_stats['mean'] = data.mean(axis = 1) # mean
day_stats['std'] = data.std(axis = 1) # standard deviations

day_stats.head()

#%% [markdown]
# ### Step 11. Find the average windspeed in January for each location.  
# #### Treat January 1961 and January 1962 both as January.

#%%
data.loc[data.index.month == 1].mean()

#%% [markdown]
# ### Step 12. Downsample the record to a yearly frequency for each location.

#%%
data.groupby(data.index.to_period('A')).mean()

# OR

aa = data.resample('YS').mean()
aa.index = aa.index.to_period('A')

#%% [markdown]
# ### Step 13. Downsample the record to a monthly frequency for each location.

#%%
data.groupby(data.index.to_period('M')).mean()

#%% [markdown]
# ### Step 14. Downsample the record to a weekly frequency for each location.

#%%
data.groupby(data.index.to_period('W')).mean()

#%% [markdown]
# ### Step 15. Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 52 weeks.

#%%
# resample data to 'W' week and use the functions
weekly = data.resample('W').agg(['min','max','mean','std'])

# slice it for the first 52 weeks and locations
weekly.loc[weekly.index[1:53], "RPT":"MAL"] .head(10)


