#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '02_Filtering_&_Sorting\Euro12'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Ex2 - Filtering and Sorting Data
#%% [markdown]
# This time we are going to pull data directly from the internet.
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv). 
#%% [markdown]
# ### Step 3. Assign it to a variable called euro12.

#%%
euro12 = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv', sep=',')
euro12

#%% [markdown]
# ### Step 4. Select only the Goal column.

#%%
euro12.Goals

#%% [markdown]
# ### Step 5. How many team participated in the Euro2012?

#%%
euro12.shape[0]

#%% [markdown]
# ### Step 6. What is the number of columns in the dataset?

#%%
euro12.info()

#%% [markdown]
# ### Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline

#%%
# filter only giving the column names

discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
discipline

#%% [markdown]
# ### Step 8. Sort the teams by Red Cards, then to Yellow Cards

#%%
discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)

#%% [markdown]
# ### Step 9. Calculate the mean Yellow Cards given per Team

#%%
round(discipline['Yellow Cards'].mean())

#%% [markdown]
# ### Step 10. Filter teams that scored more than 6 goals

#%%
euro12[euro12.Goals > 6]

#%% [markdown]
# ### Step 11. Select the teams that start with G

#%%
euro12[euro12.Team.str.startswith('G')]

#%% [markdown]
# ### Step 12. Select the first 7 columns

#%%
# use .iloc to slices via the position of the passed integers
# : means all, 0:7 means from 0 to 7

euro12.iloc[: , 0:7]

#%% [markdown]
# ### Step 13. Select all columns except the last 3.

#%%
# use negative to exclude the last 3 columns

euro12.iloc[: , :-3]

#%% [markdown]
# ### Step 14. Present only the Shooting Accuracy from England, Italy and Russia

#%%
# .loc is another way to slice, using the labels of the columns and indexes

euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]


