import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy

df = pd.read_excel('1 StatSspace/result_zen_fix_col1.xlsx', index_col='region')
a = ['1 квартал 2015', '2 квартал 2015', '3 квартал 2015', '4 квартал 2015', '1 квартал 2016', '2 квартал 2016',
     '3 квартал 2016', '4 квартал 2016', '1 квартал 2017', '2 квартал 2017', '3 квартал 2017',
     '4 квартал 2017', '1 квартал 2018', '2 квартал 2018', '3 квартал 2018', '4 квартал 2018',
     '1 квартал 2019', '2 квартал 2019', '3 квартал 2019', '4 квартал 2019', '1 квартал 2020', '2 квартал 2020',
     '3 квартал 2020', '4 квартал 2020', ]
d = {'region': df.index}
for i in range(0, len(df.columns), 3):
    for j in range(len(df[df.columns[i]])):
        k = 0
        t = 3
        for m in range(3):
            if i + m < len(df.columns) and df[df.columns[i + m]][j] > 0:
                k += df[df.columns[i + m]][j]
            else:
                t -= 1
        if t != 0:
            k /= t
        if a[i // 3] in d:
            d[a[i // 3]].append(k)
        else:
            d[a[i // 3]] = [k]

if numpy.NAN in d:
    d.pop(numpy.NAN)
df_1 = pd.DataFrame(d)
df_1.to_excel('Tables/стоимость потребительской корзины по кварталам.xlsx', index=False)
# df_1.plot()
# plt.show()
