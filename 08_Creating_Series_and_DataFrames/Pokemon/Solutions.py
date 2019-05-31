#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '08_Creating_Series_and_DataFrames\\Pokemon'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Pokemon
#%% [markdown]
# ### Introduction:
# 
# This time you will create the data.
# 
# 
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd

#%% [markdown]
# ### Step 2. Create a data dictionary

#%%
raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'],
            "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no','yes','no']                        
            }

#%% [markdown]
# ### Step 3. Assign it to a variable called 

#%%
pokemon = pd.DataFrame(raw_data)
pokemon.head()

#%% [markdown]
# ### Step 4. Ops...it seems the DataFrame columns are in alphabetical order. Place  the order of the columns as name, type, hp, evolution, pokedex

#%%
pokemon = pokemon[['name', 'type', 'hp', 'evolution','pokedex']]
pokemon

#%% [markdown]
# ### Step 5. Add another column called place, and insert what you have in mind.

#%%
pokemon['place'] = ['park','street','lake','forest']
pokemon

#%% [markdown]
# ### Step 6. Present the type of each column

#%%
pokemon.dtypes

#%% [markdown]
# ### BONUS: Create your own question and answer it.

#%%

