#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '02_Filtering_&_Sorting\Fictional Army'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Fictional Army - Filtering and Sorting
#%% [markdown]
# ### Introduction:
# 
# This exercise was inspired by this [page](http://chrisalbon.com/python/)
# 
# Special thanks to: https://github.com/chrisalbon for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd

#%% [markdown]
# ### Step 2. This is the data given as a dictionary

#%%
# Create an example dataframe about a fictional army
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

#%% [markdown]
# ### Step 3. Create a dataframe and assign it to a variable called army. 
# 
# #### Don't forget to include the columns names in the order presented in the dictionary ('regiment', 'company', 'deaths'...) so that the column index order is consistent with the solutions. If omitted, pandas will order the columns alphabetically.

#%%
army = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'deaths', 'battles', 'size', 'veterans', 'readiness', 'armored', 'deserters', 'origin'])

#%% [markdown]
# ### Step 4. Set the 'origin' colum as the index of the dataframe

#%%
army = army.set_index('origin')
army

#%% [markdown]
# ### Step 5. Print only the column veterans

#%%
army['veterans']

#%% [markdown]
# ### Step 6. Print the columns 'veterans' and 'deaths'

#%%
army[['veterans', 'deaths']]

#%% [markdown]
# ### Step 7. Print the name of all the columns.

#%%
army.columns

#%% [markdown]
# ### Step 8. Select the 'deaths', 'size' and 'deserters' columns from Maine and Alaska

#%%
# Select all rows with the index label "Maine" and "Alaska"
army.loc[['Maine','Alaska'] , ["deaths","size","deserters"]]

#%% [markdown]
# ### Step 9. Select the rows 3 to 7 and the columns 3 to 6

#%%
#
army.iloc[3:7, 3:6]

#%% [markdown]
# ### Step 10. Select every row after the fourth row

#%%
army.iloc[3:]

#%% [markdown]
# ### Step 11. Select every row up to the 4th row

#%%
army.iloc[:3]

#%% [markdown]
# ### Step 12. Select the 3rd column up to the 7th column

#%%
# the first : means all
# after the comma you select the range

army.iloc[: , 4:7]

#%% [markdown]
# ### Step 13. Select rows where df.deaths is greater than 50

#%%
army[army['deaths'] > 50]

#%% [markdown]
# ### Step 14. Select rows where df.deaths is greater than 500 or less than 50

#%%
army[(army['deaths'] > 500) | (army['deaths'] < 50)]

#%% [markdown]
# ### Step 15. Select all the regiments not named "Dragoons"

#%%
army[(army['regiment'] != 'Dragoons')]

#%% [markdown]
# ### Step 16. Select the rows called Texas and Arizona

#%%
army.loc[['Arizona', 'Texas']]

#%% [markdown]
# ### Step 17. Select the third cell in the row named Arizona

#%%
army.loc[['Arizona'], ['deaths']]

#OR

army.iloc[[0], army.columns.get_loc('deaths')]

#%% [markdown]
# ### Step 18. Select the third cell down in the column named deaths

#%%
army.loc['Texas', 'deaths']

#OR

army.iloc[[2], army.columns.get_loc('deaths')]


