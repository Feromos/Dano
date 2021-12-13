import pandas as pd
from statsmodels.tsa.stattools import adfuller
from numpy import log

df = pd.read_excel('Tables/безработица по кварталам.xlsx', index_col='region')
# df = pd.read_excel('Tables/индекс цен по кварталам.xlsx', index_col='region')
# df = pd.read_excel('Tables/разводы по кварталам.xlsx', index_col='region')
# df = pd.read_excel('Tables/безработица по кварталам.xlsx', index_col='region')

d = {'all time': []}
for i in df:
    for j in df[i]:
        if j != 0:
            d['all time'].append(log(j))
result = adfuller((d['all time']))
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
    print('\t%s: %.3f' % (key, value))
