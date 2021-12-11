import csv
import pandas as pd
import matplotlib.pyplot as plt
from numpy import log
import numpy

df_1 = pd.read_excel('Tables/количество разводов на 1 брак.xlsx', index_col='region')
df_2 = pd.read_excel('Tables/количество потребительских корзин за зарплату.xlsx', index_col='region')
a = df_1.index
d1 = {
    'time': ['1 квартал 2015', '2 квартал 2015', '3 квартал 2015', '4 квартал 2015', '1 квартал 2016', '2 квартал 2016',
             '3 квартал 2016', '4 квартал 2016', '1 квартал 2017', '2 квартал 2017', '3 квартал 2017',
             '4 квартал 2017', '1 квартал 2018', '2 квартал 2018', '3 квартал 2018', '4 квартал 2018',
             '1 квартал 2019', '2 квартал 2019', '3 квартал 2019', '4 квартал 2019', '1 квартал 2020', '2 квартал 2020',
             '3 квартал 2020', '4 квартал 2020', ]}
for i in df_1:
    for j in range(len(a)):
        if df_1[i][j] > 0:
            if a[j] in d1:
                d1[a[j]].append(df_1[i][j])
            else:
                d1[a[j]] = [df_1[i][j]]
        else:
            if a[j] in d1:
                d1[a[j]].append(0)
            else:
                d1[a[j]] = [0]
if numpy.NAN in d1:
    d1.pop(numpy.NAN)
d2 = {
    'time': ['1 квартал 2015', '2 квартал 2015', '3 квартал 2015', '4 квартал 2015', '1 квартал 2016', '2 квартал 2016',
             '3 квартал 2016', '4 квартал 2016', '1 квартал 2017', '2 квартал 2017', '3 квартал 2017',
             '4 квартал 2017', '1 квартал 2018', '2 квартал 2018', '3 квартал 2018', '4 квартал 2018',
             '1 квартал 2019', '2 квартал 2019', '3 квартал 2019', '4 квартал 2019', '1 квартал 2020', '2 квартал 2020',
             '3 квартал 2020', '4 квартал 2020', ]}
a = df_2.index
for i in df_2:
    for j in range(len(a)):
        if df_2[i][j] > 0:
            if a[j] in d2:
                d2[a[j]].append(log(df_2[i][j]))
            else:
                d2[a[j]] = [log(df_2[i][j])]
        else:
            if a[j] in d2:
                d2[a[j]].append(0)
            else:
                d2[a[j]] = [0]
if numpy.NAN in d2:
    d2.pop(numpy.NAN)
d1.pop('Республика Крым')
d1.pop('г.Севастополь')
df_3 = pd.DataFrame(d1)
df_4 = pd.DataFrame(d2)
for i in d2:
    if i == 'time':
        d1[i] = d1[i] + ['разводы'] + d2[i]
    else:
        d1[i] = d1[i] + [numpy.NAN] + d2[i]
for i in df_3:
    m = 0
    if i != 'time':
        for j in range(len(df_3[i])):
            if df_3[i][j] != 0 and df_4[i][j] != 0:
                m += 1
            else:
                break
        d1[i] += [numpy.NAN, df_3[i][:m].corr(df_4[i][:m])]
d1['time'] += ['корзины', 'Корреляция']
df_5 = pd.DataFrame(d1)
df_5.to_excel('Tables/корреляция_корзины_разводы(на 1 брак).xlsx', index=False)
