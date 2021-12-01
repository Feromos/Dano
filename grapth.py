import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy

df_1 = pd.read_excel('Tables/жилье_1.xlsx', index_col='time')
df_2 = pd.read_excel('Tables/браки.xlsx', index_col='time')
df_3 = pd.DataFrame({'цены на первичном рынку жилья': df_1['Белгородская область'],
                     'Число браков': df_2['Белгородская область']})
df_3.plot()
plt.show()
