#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '04_Apply\Students_Alcohol_Consumption'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Student Alcohol Consumption
#%% [markdown]
# ### Introduction:
# 
# This time you will download a dataset from the UCI.
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd
import numpy

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv).
#%% [markdown]
# ### Step 3. Assign it to a variable called df.

#%%
csv_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(csv_url)
df.head()

#%% [markdown]
# ### Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column

#%%
stud_alcoh = df.loc[: , "school":"guardian"]
stud_alcoh.head()

#%% [markdown]
# ### Step 5. Create a lambda function that capitalize strings.

#%%
capitalizer = lambda x: x.capitalize()

#%% [markdown]
# ### Step 6. Capitalize both Mjob and Fjob

#%%
stud_alcoh['Mjob'].apply(capitalizer)
stud_alcoh['Fjob'].apply(capitalizer)

#%% [markdown]
# ### Step 7. Print the last elements of the data set.

#%%
stud_alcoh.tail()

#%% [markdown]
# ### Step 8. Did you notice the original dataframe is still lowercase? Why is that? Fix it and capitalize Mjob and Fjob.

#%%
stud_alcoh['Mjob'] = stud_alcoh['Mjob'].apply(capitalizer)
stud_alcoh['Fjob'] = stud_alcoh['Fjob'].apply(capitalizer)
stud_alcoh.tail()

#%% [markdown]
# ### Step 9. Create a function called majority that return a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)

#%%
def majority(x):
    if x > 17:
        return True
    else:
        return False


#%%
stud_alcoh['legal_drinker'] = stud_alcoh['age'].apply(majority)
stud_alcoh.head()

#%% [markdown]
# ### Step 10. Multiply every number of the dataset by 10. 
# ##### I know this makes no sense, don't forget it is just an exercise

#%%
def times10(x):
    if type(x) is int:
        return 10 * x
    return x


#%%
stud_alcoh.applymap(times10).head(10)


