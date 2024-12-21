import pandas as pd
import numpy as np


df = pd.read_csv('DataMiningDataSetContainsNan.csv')

mean_value = round(df['Yas'].mean()) 


df['Yas'] = df['Yas'].fillna(mean_value)


df.loc[df['Yas'] <= 20, 'IngilizceBilme'] = 0
df.loc[(df['Yas'] > 20) & (df['Yas'] <= 40), 'IngilizceBilme'] = 1
df.loc[df['Yas'] > 40, 'IngilizceBilme'] = 2


df.to_csv('DataMiningDataSetContainsMeanInsteadOfNan.csv', index=False)
