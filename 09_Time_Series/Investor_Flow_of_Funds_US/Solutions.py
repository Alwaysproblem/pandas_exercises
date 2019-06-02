#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '09_Time_Series\\Investor_Flow_of_Funds_US'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Investor - Flow of Funds - US
#%% [markdown]
# ### Introduction:
# 
# Special thanks to: https://github.com/rgrp for sharing the dataset.
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv). 
#%% [markdown]
# ### Step 3. Assign it to a variable called 

#%%
url = 'https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv'
df = pd.read_csv(url)
df.head()

#%% [markdown]
# ### Step 4.  What is the frequency of the dataset?

#%%
# weekly data

#%% [markdown]
# ### Step 5. Set the column Date as the index.

#%%
df = df.set_index('Date')
df.head()

#%% [markdown]
# ### Step 6. What is the type of the index?

#%%
df.index
# it is a 'object' type

#%% [markdown]
# ### Step 7. Set the index to a DatetimeIndex type

#%%
df.index = pd.to_datetime(df.index)
type(df.index)

#%% [markdown]
# ### Step 8.  Change the frequency to monthly, sum the values and assign it to monthly.

#%%
monthly = df.resample('M').sum()
monthly

#%% [markdown]
# ### Step 9. You will notice that it filled the dataFrame with months that don't have any data with NaN. Let's drop these rows.

#%%
monthly = monthly.dropna()
monthly

#%% [markdown]
# ### Step 10. Good, now we have the monthly data. Now change the frequency to year.

#%%
year = monthly.resample('AS-JAN').sum()
year

#%% [markdown]
# ### BONUS: Create your own question and answer it.

#%%



