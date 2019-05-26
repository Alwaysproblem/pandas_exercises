#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), '01_Getting_&_Knowing_Your_Data\World Food Facts'))
    print(os.getcwd())
except:
    pass
#%% [markdown]
# # Ex1 - Getting and knowing your Data
#%% [markdown]
# ### Step 1. Go to https://www.kaggle.com/openfoodfacts/world-food-facts/data
#%% [markdown]
# ###  Step 2. Download the dataset to your computer and unzip it.

#%%
import pandas as pd
import numpy as np

#%% [markdown]
# ### Step 3. Use the tsv file and assign it to a dataframe called food

#%%
food = pd.read_csv('~/Desktop/en.openfoodfacts.org.products.tsv', sep='\t')
#%% [markdown]
# ### Step 4. See the first 5 entries

#%%
food.head()

#%% [markdown]
# ### Step 5. What is the number of observations in the dataset?

#%%
food.shape #will give you both (observations/rows, columns)


#%%
food.shape[0] #will give you only the observations/rows number

#%% [markdown]
# ### Step 6. What is the number of columns in the dataset?

#%%
print(food.shape) #will give you both (observations/rows, columns)
print(food.shape[1]) #will give you only the columns number

#OR

food.info() #Columns: 163 entries

#%% [markdown]
# ### Step 7. Print the name of all the columns.

#%%
food.columns

#%% [markdown]
# ### Step 8. What is the name of 105th column?

#%%
food.columns[104]

#%% [markdown]
# ### Step 9. What is the type of the observations of the 105th column?

#%%
food.dtypes['-glucose_100g']

#%% [markdown]
# ### Step 10. How is the dataset indexed?

#%%
food.index

#%% [markdown]
# ### Step 11. What is the product name of the 19th observation?

#%%
food.values[18][7]


