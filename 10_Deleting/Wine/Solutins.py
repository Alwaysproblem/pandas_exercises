#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '10_Deleting\\Wine'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Wine
#%% [markdown]
# ### Introduction:
# 
# This exercise is a adaptation from the UCI Wine dataset.
# The only pupose is to practice deleting data with pandas.
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd
import numpy as np

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data). 
#%% [markdown]
# ### Step 3. Assign it to a variable called wine

#%%
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
wine = pd.read_csv(url)

wine.head()

#%% [markdown]
# ### Step 4. Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns

#%%
wine = wine.drop(wine.columns[[0,3,6,8,11,12,13]], axis = 1)

wine.head()

#%% [markdown]
# ### Step 5. Assign the columns as below:
# 
# The attributes are (dontated by Riccardo Leardi, riclea '@' anchem.unige.it):  
# 1) alcohol  
# 2) malic_acid  
# 3) alcalinity_of_ash  
# 4) magnesium  
# 5) flavanoids  
# 6) proanthocyanins  
# 7) hue 

#%%
wine.columns = ['alcohol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 'flavanoids', 'proanthocyanins', 'hue']
wine.head()

#%% [markdown]
# ### Step 6. Set the values of the first 3 rows from alcohol as NaN

#%%
wine.iloc[0:3, 0] = np.nan
wine.head()

#%% [markdown]
# ### Step 7. Now set the value of the rows 3 and 4 of magnesium as NaN

#%%
wine.iloc[2:4, 3] = np.nan
wine.head()

#%% [markdown]
# ### Step 8. Fill the value of NaN with the number 10 in alcohol and 100 in magnesium

#%%
wine.alcohol.fillna(10, inplace = True)

wine.magnesium.fillna(100, inplace = True)

wine.head()

#%% [markdown]
# ### Step 9. Count the number of missing values

#%%
wine.isnull().sum()

#%% [markdown]
# ### Step 10.  Create an array of 10 random numbers up until 10

#%%
random = np.random.randint(10, size = 10)
random

#%% [markdown]
# ### Step 11.  Use random numbers you generated as an index and assign NaN value to each of cell.

#%%
wine.alcohol[random] = np.nan
wine.head(10)

#%% [markdown]
# ### Step 12.  How many missing values do we have?

#%%
wine.isnull().sum()

#%% [markdown]
# ### Step 13. Delete the rows that contain missing values

#%%
wine = wine.dropna(axis = 0, how = "any")
wine.head()

#%% [markdown]
# ### Step 14. Print only the non-null values in alcohol

#%%
mask = wine.alcohol.notnull()
mask


#%%
wine.alcohol[mask]

#%% [markdown]
# ### Step 15.  Reset the index, so it starts with 0 again

#%%
wine = wine.reset_index(drop = True)
wine.head()

#%% [markdown]
# ### BONUS: Create your own question and answer it.

#%%



