#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '03_Grouping\Alcohol_Consumption'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Ex - GroupBy
#%% [markdown]
# ### Introduction:
# 
# GroupBy can be summarizes as Split-Apply-Combine.
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# Check out this [Diagram](http://i.imgur.com/yjNkiwL.png)  
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv). 
#%% [markdown]
# ### Step 3. Assign it to a variable called drinks.

#%%
drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
drinks.head()

#%% [markdown]
# ### Step 4. Which continent drinks more beer on average?

#%%
drinks.groupby('continent').beer_servings.mean()

#%% [markdown]
# ### Step 5. For each continent print the statistics for wine consumption.

#%%
drinks.groupby('continent').wine_servings.describe()

#%% [markdown]
# ### Step 6. Print the mean alcoohol consumption per continent for every column

#%%
drinks.groupby('continent').mean()

#%% [markdown]
# ### Step 7. Print the median alcoohol consumption per continent for every column

#%%
drinks.groupby('continent').median()

#%% [markdown]
# ### Step 8. Print the mean, min and max values for spirit consumption.
# #### This time output a DataFrame

#%%
drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max'])


