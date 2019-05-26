#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), '01_Getting_&_Knowing_Your_Data\Occupation'))
    print(os.getcwd())
except:
    pass
#%% [markdown]
# # Ex3 - Getting and Knowing your Data
#%% [markdown]
# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 
#%% [markdown]
# ### Step 3. Assign it to a variable called users and use the 'user_id' as index

#%%
users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', 
                      sep='|', index_col='user_id')

#%% [markdown]
# ### Step 4. See the first 25 entries

#%%
users.head(25)

#%% [markdown]
# ### Step 5. See the last 10 entries

#%%
users.tail(10)

#%% [markdown]
# ### Step 6. What is the number of observations in the dataset?

#%%
users.shape[0]

#%% [markdown]
# ### Step 7. What is the number of columns in the dataset?

#%%
users.shape[1]

#%% [markdown]
# ### Step 8. Print the name of all the columns.

#%%
users.columns

#%% [markdown]
# ### Step 9. How is the dataset indexed?

#%%
# "the index" (aka "the labels")
users.index

#%% [markdown]
# ### Step 10. What is the data type of each column?

#%%
users.dtypes

#%% [markdown]
# ### Step 11. Print only the occupation column

#%%
users.occupation 

#OR

users['occupation']

#%% [markdown]
# ### Step 12. How many different occupations there are in this dataset?

#%%
users.occupation.nunique()

#%% [markdown]
# ### Step 13. What is the most frequent occupation?

#%%
users.occupation.value_counts().head()

#%% [markdown]
# ### Step 14. Summarize the DataFrame.

#%%
users.describe() #Notice: By default, only the numeric columns are returned. 

#%% [markdown]
# ### Step 15. Summarize all the columns

#%%
users.describe(include = "all") #Notice: By default, only the numeric columns are returned.


#%% [markdown]
# ### Step 16. Summarize only the occupation column

#%%
users.occupation.describe()

#%% [markdown]
# ### Step 17. What is the mean age of users?

#%%
round(users.age.mean())

#%% [markdown]
# ### Step 18. What is the age with least occurrence?

#%%
users.age.value_counts().tail() #7, 10, 11, 66 and 73 years -> only 1 occurrence
