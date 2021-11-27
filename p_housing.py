import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy

df = pd.read_excel('1 StatSspace/result_zen-jil_col1.xlsx', index_col='region')
a = df.index
d = {
    'time': ['1 квартал 2015', '2 квартал 2015', '3 квартал 2015', '4 квартал 2015', '1 квартал 2016', '2 квартал 2016',
             '3 квартал 2016', '4 квартал 2016', '1 квартал 2017', '2 квартал 2017', '3 квартал 2017',
             '4 квартал 2017', '1 квартал 2018', '2 квартал 2018', '3 квартал 2018', '4 квартал 2018',
             '1 квартал 2019', '2 квартал 2019', '3 квартал 2019', '4 квартал 2019', '1 квартал 2020', '2 квартал 2020',
             '3 квартал 2020', '4 квартал 2020', ]}
for i in df:
    for j in range(len(a)):
        if df[i][j] > 0:
            if a[j] in d:
                d[a[j]].append(df[i][j])
            else:
                d[a[j]] = [df[i][j]]
        else:
            if a[j] in d:
                d[a[j]].append(0)
            else:
                d[a[j]] = [0]
if numpy.NAN in d:
    d.pop(numpy.NAN)
for i in d:
    if i != 'time':
        r = [100]
        for j in range(1, len(d[i])):
            k = j - 1
            while k > -1 and d[i][k] == 0:
                k -= 1
            if k != -1:
                r.append((d[i][j] - d[i][k]) / d[i][k] * 10000)
            else:
                r.append(100)
        d[i] = r
df_1 = pd.DataFrame(d)
df_1.to_excel('Tables/жилье_1.xlsx', index=False)
# df_1.plot()
# plt.show()
