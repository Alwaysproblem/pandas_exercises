import pandas as pd
import numpy as np

dt = {
    'f': 'Int64', 
    'd': np.object,
    "c": np.float
}

nan_dic = {
    'f': 'NAN',
    'd': 'NAN',
    'c': 'NAN'
}

df = pd.read_csv('./data/Toy.csv', sep=',')

print(f'original dataframe: \n{df}')

df['f'] = pd.to_numeric(df['f'], errors='coerce').astype('Int64')
df['c'] = pd.to_numeric(df['c'], errors='coerce')

print(f'after parsing dataframe with to_numeric:\n{df}')

def float_converter(num):
    try:
        return np.float(num)
    except:
        return np.nan
    
def Int_converter(integer):
    try:
        return np.int(integer)
    except:
        return 0
    

df = pd.read_csv('./data/Toy.csv', sep=',', converters={'f': Int_converter, 'c': float_converter})
# df = pd.read_csv('./data/Toy.csv', sep=',', dtype=dt)

print(f'after parsing dataframe with converters:\n{df}')
