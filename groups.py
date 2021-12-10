import csv
import pandas as pd
import matplotlib.pyplot as plt
from numpy import log
import numpy

df_1 = pd.read_excel('Tables/количество потребительских корзин за зарплату(со средним).xlsx', index_col='region')
df_2 = pd.read_excel('Tables/разводы по кварталам.xlsx', index_col='region')
a = df_1.index
c = df_2.index
d1 = {
    'time': ['1 квартал 2015', '2 квартал 2015', '3 квартал 2015', '4 квартал 2015', '1 квартал 2016', '2 квартал 2016',
             '3 квартал 2016', '4 квартал 2016', '1 квартал 2017', '2 квартал 2017', '3 квартал 2017',
             '4 квартал 2017', '1 квартал 2018', '2 квартал 2018', '3 квартал 2018', '4 квартал 2018',
             '1 квартал 2019', '2 квартал 2019', '3 квартал 2019', '4 квартал 2019', '1 квартал 2020', '2 квартал 2020',
             '3 квартал 2020', '4 квартал 2020', ]}
b = []
for i in a:
    if type(i) == str:
        b.append(i)
a = b[:]


def find1(r):
    global a, c
    for i in range(len(c)):
        if c[i] == a[r]:
            return i


for i in df_1:
    if i != 'Среднее':
        for k in range(len(a)):
            j = find1(k)
            if df_2[i][j] > 0:
                if a[k] in d1:
                    d1[a[k]].append(df_2[i][j])
                else:
                    d1[a[k]] = [df_2[i][j]]
            else:
                if a[k] in d1:
                    d1[a[k]].append(0)
                else:
                    d1[a[k]] = [0]
if numpy.NAN in d1:
    d1.pop(numpy.NAN)
df_5 = pd.DataFrame(d1)
df_5.to_excel('Tables/разводы по кварталам(группы).xlsx', index=False)
