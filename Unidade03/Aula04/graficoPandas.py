import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Produto':['A', 'B', 'C'],
    'qtde_vendida': [33, 200, 12]
}

df= pd.DataFrame(dados)

df.plot(x='Produto', y='qtde_vendida', kind='bar')
df.plot(x='Produto', y='qtde_vendida', kind='pie')
df.plot(x='Produto', y='qtde_vendida', kind='line')

plt.show()