import csv
import pandas as pd
import matplotlib.pyplot as plt
from numpy import log
import numpy

df_1 = pd.read_excel('Tables/количество потребительских корзин за зарплату(группы).xlsx', index_col='time')
for i in df_1:
    if i != numpy.NAN:
        for j in range(len(df_1[i])):
            if df_1[i][j] == 0:
                df_1[i][j] = numpy.NAN
df_1.to_excel('Tables/количество потребительских корзин за зарплату(группы).xlsx', index=False)
