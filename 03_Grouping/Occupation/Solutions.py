#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '03_Grouping\Occupation'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Occupation
#%% [markdown]
# ### Introduction:
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 
#%% [markdown]
# ### Step 3. Assign it to a variable called users.

#%%
users = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', 
                      sep='|', index_col='user_id')
users.head()

#%% [markdown]
# ### Step 4. Discover what is the mean age per occupation

#%%
users.groupby('occupation').age.mean()

#%% [markdown]
# ### Step 5. Discover the Male ratio per occupation and sort it from the most to the least

#%%
# create a function
def gender_to_numeric(x):
    if x == 'M':
        return 1
    if x == 'F':
        return 0

# apply the function to the gender column and create a new column
users['gender_n'] = users['gender'].apply(gender_to_numeric)


a = users.groupby('occupation').gender_n.sum() / users.occupation.value_counts() * 100 

# sort to the most male 
a.sort_values(ascending = False)

#%% [markdown]
# ### Step 6. For each occupation, calculate the minimum and maximum ages

#%%
users.groupby('occupation').age.agg(['min', 'max'])

#%% [markdown]
# ### Step 7. For each combination of occupation and gender, calculate the mean age

#%%
users.groupby(['occupation', 'gender']).age.mean()

#%% [markdown]
# ### Step 8.  For each occupation present the percentage of women and men

#%%
# create a data frame and apply count to gender
gender_ocup = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})

# create a DataFrame and apply count for each occupation
occup_count = users.groupby(['occupation']).agg('count')

# divide the gender_ocup per the occup_count and multiply per 100
occup_gender = gender_ocup.div(occup_count, level = "occupation") * 100

# present all rows from the 'gender column'
occup_gender.loc[: , 'gender']


