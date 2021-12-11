import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy

df_1 = pd.read_excel('Tables/разводы по кварталам.xlsx', index_col='region')
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
df_3 = pd.DataFrame({'г.Москва': d1['г.Москва']})
df_3.plot()
plt.show()
