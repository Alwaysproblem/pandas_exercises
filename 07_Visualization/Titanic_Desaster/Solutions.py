#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '07_Visualization\\Titanic_Desaster'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Visualizing the Titanic Disaster
#%% [markdown]
# ### Introduction:
# 
# This exercise is based on the titanic Disaster dataset avaiable at [Kaggle](https://www.kaggle.com/c/titanic).  
# To know more about the variables check [here](https://www.kaggle.com/c/titanic/data)
# 
# 
# ### Step 1. Import the necessary libraries

#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

#%% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/Visualization/Titanic_Desaster/train.csv). 
#%% [markdown]
# ### Step 3. Assign it to a variable titanic 

#%%
url = 'train.csv'

titanic = pd.read_csv(url)

titanic.head()

#%% [markdown]
# ### Step 4. Set PassengerId as the index 

#%%
titanic.set_index('PassengerId').head()

#%% [markdown]
# ### Step 5. Create a pie chart presenting the male/female proportion

#%%
# sum the instances of males and females
males = (titanic['Sex'] == 'male').sum()
females = (titanic['Sex'] == 'female').sum()

# put them into a list called proportions
proportions = [males, females]

# Create a pie chart
plt.pie(
    # using proportions
    proportions,
    
    # with the labels being officer names
    labels = ['Males', 'Females'],
    
    # with no shadows
    shadow = False,
    
    # with colors
    colors = ['blue','red'],
    
    # with one slide exploded out
    explode = (0.15 , 0),
    
    # with the start angle at 90%
    startangle = 90,
    
    # with the percent listed as a fraction
    autopct = '%1.1f%%'
    )

# View the plot drop above
plt.axis('equal')

# Set labels
plt.title("Sex Proportion")

# View the plot
plt.tight_layout()
plt.show()

#%% [markdown]
# ### Step 6. Create a scatterplot with the Fare payed and the Age, differ the plot color by gender

#%%
# creates the plot using
lm = sns.lmplot(x = 'Age', y = 'Fare', data = titanic, hue = 'Sex', fit_reg=False)

# set title
lm.set(title = 'Fare x Age')

# get the axes object and tweak it
axes = lm.axes
axes[0,0].set_ylim(-5,)
axes[0,0].set_xlim(-5,85)

#%% [markdown]
# ### Step 7. How many people survived?

#%%
titanic.Survived.sum()

#%% [markdown]
# ### Step 8. Create a histogram with the Fare payed

#%%
# sort the values from the top to the least value and slice the first 5 items
df = titanic.Fare.sort_values(ascending = False)
df

# create bins interval using numpy
binsVal = np.arange(0,600,10)
binsVal

# create the plot
plt.hist(df, bins = binsVal)

# Set the title and labels
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.title('Fare Payed Histrogram')

# show the plot
plt.show()

#%% [markdown]
# ### BONUS: Create your own question and answer it.

#%%



