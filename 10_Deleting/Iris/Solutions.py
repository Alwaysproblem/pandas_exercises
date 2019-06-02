#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '10_Deleting\\Iris'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Iris
#%% [markdown]
# ### Introduction:
# 
# This exercise may seem a little bit strange, but keep doing it.
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd
import numpy as np

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data). 
#%% [markdown]
# ### Step 3. Assign it to a variable called iris

#%%
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url)

iris.head()

#%% [markdown]
# ### Step 4. Create columns for the dataset

#%%
# 1. sepal_length (in cm)
# 2. sepal_width (in cm)
# 3. petal_length (in cm)
# 4. petal_width (in cm)
# 5. class

iris.columns = ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'class']
iris.head()

#%% [markdown]
# ### Step 5.  Is there any missing value in the dataframe?

#%%
pd.isnull(iris).sum()
# nice no missing value

#%% [markdown]
# ### Step 6.  Lets set the values of the rows 10 to 29 of the column 'petal_length' to NaN

#%%
iris.iloc[10:30,2:3] = np.nan
iris.head(20)

#%% [markdown]
# ### Step 7. Good, now lets substitute the NaN values to 1.0

#%%
iris.petal_length.fillna(1, inplace = True)
iris

#%% [markdown]
# ### Step 8. Now let's delete the column class

#%%
del iris['class']
iris.head()

#%% [markdown]
# ### Step 9.  Set the first 3 rows as NaN

#%%
iris.iloc[0:3 ,:] = np.nan
iris.head()

#%% [markdown]
# ### Step 10.  Delete the rows that have NaN

#%%
iris = iris.dropna(how='any')
iris.head()

#%% [markdown]
# ### Step 11. Reset the index so it begins with 0 again

#%%
iris = iris.reset_index(drop = True)
iris.head()

#%% [markdown]
# ### BONUS: Create your own question and answer it.

#%%



