import pandas as pd
import numpy as np
url="https://raw.githubusercontent.com/cognizance-amrita/AI-Tasks/main/Task-1/Q2-Dataset.csv"
df=pd.read_csv(url)
df=df.set_index(['Id'])
df=df.replace(np.NaN,0)
df.to_csv('DataSet-2.csv')
JustCheck=df.head()
print(JustCheck)
