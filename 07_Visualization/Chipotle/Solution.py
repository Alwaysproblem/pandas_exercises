#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '07_Visualization\Chipotle'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Visualizing Chipotle's Data
#%% [markdown]
# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt 

# from IPython import get_ipython
# # set this so the 
# get_ipython().run_line_magic('matplotlib', 'inline')

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
# ### Step 5. Create a histogram of the top 5 items bought

#%%
# get the Series of the names
x = chipo.item_name

# use the Counter class from collections to create a dictionary with keys(text) and frequency
letter_counts = Counter(x)

# convert the dictionary to a DataFrame
df = pd.DataFrame.from_dict(letter_counts, orient='index')

# sort the values from the top to the least value and slice the first 5 items
df = df[0].sort_values(ascending = True)[45:50]

# create the plot
df.plot(kind='bar')

# Set the title and labels
plt.xlabel('Items')
plt.ylabel('Price')
plt.title('Most ordered Chipotle\'s Items')

# show the plot
plt.show()

#%% [markdown]
# ### Step 6. Create a scatterplot with the number of items orderered per order price
# #### Hint: Price should be in the X-axis and Items ordered in the Y-axis

#%%
# create a list of prices
chipo.item_price = [float(value[1:-1]) for value in chipo.item_price] # strip the dollar sign and trailing space

# then groupby the orders and sum
orders = chipo.groupby('order_id').sum()

# creates the scatterplot
# plt.scatter(orders.quantity, orders.item_price, s = 50, c = 'green')
# plt.scatter(x = orders.item_price, y = orders.quantity, s = 50, c = 'green')

# # Set the title and labels
# plt.xlabel('Order Price')
# plt.ylabel('Items ordered')
# plt.title('Number of items ordered per order price')
# plt.ylim(0)

# OR

orders.plot(x= 'item_price', y= 'quantity', kind="scatter",
               title='Number of items ordered per order price', s=50, c='green')

plt.show()



#%% [markdown]
# ### BONUS: Create a question and a graph to answer your own question.

#%%



