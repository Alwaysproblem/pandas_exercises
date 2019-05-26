#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '02_Filtering_&_Sorting\Chipotle'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Ex1 - Filtering and Sorting Data
#%% [markdown]
# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 
#%% [markdown]
# ### Step 3. Assign it to a variable called chipo.

#%%
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

chipo = pd.read_csv(url, sep = '\t')

#%% [markdown]
# ### Step 4. How many products cost more than $10.00?

#%%
# clean the item_price column and transform it in a float
prices = [float(value[1 : -1]) for value in chipo.item_price]

# reassign the column with the cleaned prices
chipo.item_price = prices

# delete the duplicates in item_name and quantity
chipo_filtered = chipo.drop_duplicates(['item_name','quantity'])

# select only the products with quantity equals to 1
chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]

chipo_one_prod[chipo_one_prod['item_price']>10].item_name.nunique()

#%%
chipo.item_price = chipo.item_price.apply(lambda x: float(x[1 : -1]))

#%% [markdown]
# ### Step 5. What is the price of each item? 
# ###### print a data frame with only two columns item_name and item_price

#%%
# delete the duplicates in item_name and quantity
# chipo_filtered = chipo.drop_duplicates(['item_name','quantity'])
chipo[(chipo['item_name'] == 'Chicken Bowl') & (chipo['quantity'] == 1)]

# select only the products with quantity equals to 1
# chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]

# select only the item_name and item_price columns
# price_per_item = chipo_one_prod[['item_name', 'item_price']]

# sort the values from the most to less expensive
# price_per_item.sort_values(by = "item_price", ascending = False).head(20)

#%% [markdown]
# ### Step 6. Sort by the name of the item

#%%
chipo.item_name.sort_values()

# OR

chipo.sort_values(by = "item_name")

#%% [markdown]
# ### Step 7. What was the quantity of the most expensive item ordered?

#%%
chipo.sort_values(by = "item_price", ascending = False).head(1)

#%% [markdown]
# ### Step 8. How many times were a Veggie Salad Bowl ordered?

#%%
chipo_salad = chipo[chipo.item_name == "Veggie Salad Bowl"]

len(chipo_salad)

#%% [markdown]
# ### Step 9. How many times people orderd more than one Canned Soda?

#%%
chipo_drink_steak_bowl = chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)]
len(chipo_drink_steak_bowl)


