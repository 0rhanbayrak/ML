import pandas as pd
import numpy as np

df = pd.read_csv('DataMiningDataSet.csv') 

nan_indices = np.random.choice(df.index, size=50, replace=False) 
for row in nan_indices:
    df.loc[row, 'Yas'] = np.nan

df.to_csv('DataMiningDataSetContainsNancsv', index=False)
