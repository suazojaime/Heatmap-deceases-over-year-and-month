import pandas as pd
from datetime import datetime, timedelta, date
from matplotlib import pyplot as plt
import matplotlib
import numpy as np

import seaborn as sns

import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto32/Defunciones_std.csv',sep=',')

df['Fecha'] = df['Fecha'].astype('datetime64')
df.groupby('Fecha')['Defunciones'].sum()

hist = df.groupby(pd.Grouper(key='Fecha',freq='M'))['Defunciones'].sum()

df['Año'] = df["Fecha"].dt.year
df['Mes'] = df["Fecha"].dt.month

data = df.groupby(['Año','Mes'])['Defunciones'].sum().reset_index()

table=data.pivot(index='Año',columns='Mes',values='Defunciones')

sns.heatmap(table, cmap = 'flare')

plt.title('Fallecidos por año por mes')

plt.draw()
plt.pause(0.0001)
