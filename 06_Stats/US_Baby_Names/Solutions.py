#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '06_Stats\US_Baby_Names'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # US - Baby Names
#%% [markdown]
# ### Introduction:
# 
# We are going to use a subset of [US Baby Names](https://www.kaggle.com/kaggle/us-baby-names) from Kaggle.  
# In the file it will be names from 2004 until 2014
# 
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv). 
#%% [markdown]
# ### Step 3. Assign it to a variable called baby_names.

#%%
baby_names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
baby_names.info()

#%% [markdown]
# ### Step 4. See the first 10 entries

#%%
baby_names.head(10)

#%% [markdown]
# ### Step 5. Delete the column 'Unnamed: 0' and 'Id'

#%%
# deletes Unnamed: 0
del baby_names['Unnamed: 0']

# deletes Unnamed: 0
del baby_names['Id']

baby_names.head()

#%% [markdown]
# ### Step 6. Are there more male or female names in the dataset?

#%%
baby_names['Gender'].value_counts()

#%% [markdown]
# ### Step 7. Group the dataset by name and assign to names

#%%
# you don't want to sum the Year column, so you delete it
del baby_names["Year"]

# group the data
names = baby_names.groupby("Name").sum()

# print the first 5 observations
names.head()

# print the size of the dataset
print(names.shape)

# sort it from the biggest value to the smallest one
names.sort_values("Count", ascending = 0).head()

#%% [markdown]
# ### Step 8. How many different names exist in the dataset?

#%%
# as we have already grouped by the name, all the names are unique already. 
# get the length of names
len(names)

#%% [markdown]
# ### Step 9. What is the name with most occurrences?

#%%
names.Count.idxmax()

# OR

# names[names.Count == names.Count.max()]

#%% [markdown]
# ### Step 10. How many different names have the least occurrences?

#%%
len(names[names.Count == names.Count.min()])

#%% [markdown]
# ### Step 11. What is the median name occurrence?

#%%
names[names.Count == names.Count.median()]

#%% [markdown]
# ### Step 12. What is the standard deviation of names?

#%%
names.Count.std()

#%% [markdown]
# ### Step 13. Get a summary with the mean, min, max, std and quartiles.

#%%
names.describe()


