import pandas as pd
from statsmodels.tsa.stattools import adfuller
from numpy import log

df = pd.read_excel('Tables/разводы.xlsx', index_col='time')
# df = pd.read_excel('Tables/индекс цен по кварталам.xlsx', index_col='region')
# df = pd.read_excel('Tables/разводы по кварталам.xlsx', index_col='region')
# df = pd.read_excel('Tables/безработица по кварталам.xlsx', index_col='region')
t = True
k1 = 0
k2 = 0
for x in df:
    if x != 'time':
        result = adfuller(df[x])
        if result[0] > result[4]['1%']:
            t = False
            k2 += 1
        else:
            k1 += 1
print(t, k1, k2)
