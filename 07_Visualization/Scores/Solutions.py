#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '07_Visualization\Scores'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Scores
#%% [markdown]
# ### Introduction:
# 
# This time you will create the data.
# 
# ***Exercise based on [Chris Albon](http://chrisalbon.com/) work, the credits belong to him.***
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

#%% [markdown]
# ### Step 2. Create the DataFrame it should look like below.

#%%
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
            'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
            'female': [0, 1, 1, 0, 1],
            'age': [42, 52, 36, 24, 73], 
            'preTestScore': [4, 24, 31, 2, 3],
            'postTestScore': [25, 94, 57, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'female', 'preTestScore', 'postTestScore'])

df

#%% [markdown]
# ### Step 3. Create a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
# #### Hint: Don't forget to place the labels

#%%
plt.scatter(df.preTestScore, df.postTestScore, s=df.age)

#set labels and titles
plt.title("preTestScore x postTestScore")
plt.xlabel('preTestScore')
plt.ylabel('preTestScore')

#%% [markdown]
# ### Step 4. Create a Scatterplot of preTestScore and postTestScore.
# ### This time the size should be 4.5 times the postTestScore and the color determined by sex

#%%
plt.scatter(df.preTestScore, df.postTestScore, s= df.postTestScore * 4.5, c = df.female)

#set labels and titles
plt.title("preTestScore x postTestScore")
plt.xlabel('preTestScore')
plt.ylabel('preTestScore')

#%% [markdown]
# ### BONUS: Create your own question and answer it.

#%%



