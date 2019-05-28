#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '04_Apply\US_Crime_Rates'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # United States - Crime Rates - 1960 - 2014
#%% [markdown]
# ### Introduction:
# 
# This time you will create a data 
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

#%%
import numpy as np
import pandas as pd

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv). 
#%% [markdown]
# ### Step 3. Assign it to a variable called crime.

#%%
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"
crime = pd.read_csv(url)
crime.head()

#%% [markdown]
# ### Step 4. What is the type of the columns?

#%%
crime.info()

#%% [markdown]
# ##### Have you noticed that the type of Year is int64. But pandas has a different type to work with Time Series. Let's see it now.
# 
# ### Step 5. Convert the type of the column Year to datetime64

#%%
# pd.to_datetime(crime)
crime.Year = pd.to_datetime(crime.Year, format='%Y')
crime.info()

#%% [markdown]
# ### Step 6. Set the Year column as the index of the dataframe

#%%
crime = crime.set_index('Year', drop = True)
crime.head()

#%% [markdown]
# ### Step 7. Delete the Total column

#%%
del crime['Total']
crime.head()

#%% [markdown]
# ### Step 8. Group the year by decades and sum the values
# 
# #### Pay attention to the Population column number, summing this column is a mistake

#%%
# To learn more about .resample (https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.resample.html)
# To learn more about Offset Aliases (http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases)

# Uses resample to sum each decade
crimes = crime.resample('10AS').sum()

# Uses resample to get the max value only for the "Population" column
population = crime['Population'].resample('10AS').max()

# Updating the "Population" column
crimes['Population'] = population

crimes

#%% [markdown]
# ### Step 9. What is the mos dangerous decade to live in the US?

#%%
# apparently the 90s was a pretty dangerous time in the US
crime.idxmax(0)


