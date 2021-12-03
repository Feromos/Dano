import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy

df_1 = pd.read_excel('Tables/разводы.xlsx', index_col='time')
df_2 = pd.read_excel('Tables/индекс цен.xlsx', index_col='time')
df_3 = pd.DataFrame({'Изменение количества разводов': df_1['Брянская область'],
                     'Изменение индекса цен': df_2['Брянская область']})
df_3.plot()
plt.show()
