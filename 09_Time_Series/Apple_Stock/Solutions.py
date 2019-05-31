#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '09_Time_Series\\Apple_Stock'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Apple Stock
#%% [markdown]
# ### Introduction:
# 
# We are going to use Apple's stock price.
# 
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd
import numpy as np

# visualization
import matplotlib.pyplot as plt

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv)
#%% [markdown]
# ### Step 3. Assign it to a variable apple

#%%
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'
apple = pd.read_csv(url)

apple.head()

#%% [markdown]
# ### Step 4.  Check out the type of the columns

#%%
apple.dtypes

#%% [markdown]
# ### Step 5. Transform the Date column as a datetime type

#%%
apple.Date = pd.to_datetime(apple.Date)

apple['Date'].head()

#%% [markdown]
# ### Step 6.  Set the date as the index

#%%
apple = apple.set_index('Date')

apple.head()

#%% [markdown]
# ### Step 7.  Is there any duplicate dates?

#%%
# NO! All are unique
apple.index.is_unique

#%% [markdown]
# ### Step 8.  Ops...it seems the index is from the most recent date. Make the first entry the oldest date.

#%%
apple.sort_index(ascending = True).head()

#%% [markdown]
# ### Step 9. Get the last business day of each month

#%%
apple_month = apple.resample('BM').mean()

apple_month.head()

#%% [markdown]
# ### Step 10.  What is the difference in days between the first day and the oldest

#%%
(apple.index.max() - apple.index.min()).days

#%% [markdown]
# ### Step 11.  How many months in the data we have?

#%%
apple_months = apple.resample('BM').mean()

len(apple_months.index)

#%% [markdown]
# ### Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches

#%%
# makes the plot and assign it to a variable
appl_open = apple['Adj Close'].plot(title = "Apple Stock")

# changes the size of the graph
fig = appl_open.get_figure()
fig.set_size_inches(13.5, 9)

#%% [markdown]
# ### BONUS: Create your own question and answer it.

#%%



