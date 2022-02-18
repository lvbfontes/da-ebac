#%cd /content/da-ebac/

#%%writefile gasolina.csv
#dia,venda
#1,5.11
#2,4.99
#3,5.02
#4,5.21
#5,5.07
#6,5.09
#7,5.13
#8,5.12
#9,4.94
#10,5.03

import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('/content/da-ebac/gasolina.csv', sep=',')

gasolina_df.head()

with sns.axes_style('darkgrid'):
  grafico = sns.lineplot(x='dia', y='venda', data=gasolina_df, palette='pastel')
  grafico.set(title='Preço de Venda Gasolina', xlabel='Dia', ylabel='Preço de Venda')

fig = grafico.get_figure()

fig.savefig('gasolina.png')

#!touch gasolina.py