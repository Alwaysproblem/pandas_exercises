#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '01_Getting_&_Knowing_Your_Data\Chipotle'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Ex2 - Getting and Knowing your Data
#%% [markdown]
# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

#%%


#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 
#%% [markdown]
# ### Step 3. Assign it to a variable called chipo.

#%%


#%% [markdown]
# ### Step 4. See the first 10 entries

#%%


#%% [markdown]
# ### Step 5. What is the number of observations in the dataset?

#%%
# Solution 1


#%%
# Solution 2

#%% [markdown]
# ### Step 6. What is the number of columns in the dataset?

#%%


#%% [markdown]
# ### Step 7. Print the name of all the columns.

#%%


#%% [markdown]
# ### Step 8. How is the dataset indexed?

#%%


#%% [markdown]
# ### Step 9. Which was the most-ordered item? 

#%%


#%% [markdown]
# ### Step 10. For the most-ordered item, how many items were ordered?

#%%


#%% [markdown]
# ### Step 11. What was the most ordered item in the choice_description column?

#%%


#%% [markdown]
# ### Step 12. How many items were orderd in total?

#%%


#%% [markdown]
# ### Step 13. Turn the item price into a float
#%% [markdown]
# #### Step 13.a. Check the item price type

#%%


#%% [markdown]
# #### Step 13.b. Create a lambda function and change the type of item price

#%%


#%% [markdown]
# #### Step 13.c. Check the item price type

#%%


#%% [markdown]
# ### Step 14. How much was the revenue for the period in the dataset?

#%%


#%% [markdown]
# ### Step 15. How many orders were made in the period?

#%%


#%% [markdown]
# ### Step 16. What is the average revenue amount per order?

#%%
# Solution 1


#%%
# Solution 2

#%% [markdown]
# ### Step 17. How many different items are sold?

#%%



