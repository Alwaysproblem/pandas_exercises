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
import pandas as pd
import numpy as np

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 
#%% [markdown]
# ### Step 3. Assign it to a variable called chipo.

#%%
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    
chipo = pd.read_csv(url, sep = '\t')

#%% [markdown]
# ### Step 4. See the first 10 entries

#%%
chipo.head(10)

#%% [markdown]
# ### Step 5. What is the number of observations in the dataset?

#%%
# Solution 1

chipo.shape[0]  # entries <= 4622 observations


#%%
# Solution 2

chipo.info() # entries <= 4622 observations

#%% [markdown]
# ### Step 6. What is the number of columns in the dataset?

#%%
chipo.shape[1]

#%% [markdown]
# ### Step 7. Print the name of all the columns.

#%%
chipo.columns

#%% [markdown]
# ### Step 8. How is the dataset indexed?

#%%
chipo.index

#%% [markdown]
# ### Step 9. Which was the most-ordered item? 

#%%
c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)

#%% [markdown]
# ### Step 10. For the most-ordered item, how many items were ordered?

#%%
c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)

#%% [markdown]
# ### Step 11. What was the most ordered item in the choice_description column?

#%%
c = chipo.groupby('choice_description').sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)
# Diet Coke 159

#%% [markdown]
# ### Step 12. How many items were orderd in total?

#%%
total_items_orders = chipo.quantity.sum()
total_items_orders

#%% [markdown]
# ### Step 13. Turn the item price into a float
#%% [markdown]
# #### Step 13.a. Check the item price type

#%%
chipo.item_price.dtype

#%% [markdown]
# #### Step 13.b. Create a lambda function and change the type of item price

#%%
dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)

#%% [markdown]
# #### Step 13.c. Check the item price type

#%%
chipo.item_price.dtype

#%% [markdown]
# ### Step 14. How much was the revenue for the period in the dataset?

#%%
revenue = (chipo['quantity'] * chipo['item_price']).sum()

print('Revenue was: $' + str(np.round(revenue,2)))

#%% [markdown]
# ### Step 15. How many orders were made in the period?

#%%
orders = chipo.order_id.value_counts().count()
orders

#%% [markdown]
# ### Step 16. What is the average revenue amount per order?

#%%
# Solution 1

chipo['revenue'] = chipo['quantity'] * chipo['item_price']
order_grouped = chipo.groupby(by=['order_id']).sum()
order_grouped.mean()['revenue']


#%%
# Solution 2

chipo.groupby(by=['order_id']).sum().mean()['revenue']

#%% [markdown]
# ### Step 17. How many different items are sold?

#%%
chipo.item_name.value_counts().count()


