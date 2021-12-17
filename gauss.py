import pandas as pd
from matplotlib import pyplot
from numpy import log

# df = pd.read_excel('Tables/количество потребительских корзин за зарплату.xlsx', index_col='region')
# df = pd.read_excel('Tables/индекс цен по кварталам.xlsx', index_col='region')
# df = pd.read_excel('Tables/разводы по кварталам.xlsx', index_col='region')
df = pd.read_excel('Tables/разводы.xlsx', index_col='time')
d = {'all time': []}
for i in df:
    d['all time'] = df['Московская область']
df_1 = pd.DataFrame(d)
df_1.hist()
pyplot.show()
