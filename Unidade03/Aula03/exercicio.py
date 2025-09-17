import pandas as pd

data = {
    'nome': ['Mouse','Teclado','Fone','Processador','Memória RAM'],
    'quantidade de itens comprados': [4,4,4,2,6],
    'tipo de item': ['Periférico', 'Periférico', 'Eletrônico', 'Hardware', 'Hardware'],
    'receita total': [120, 100, 50, 300, 200]
}

df = pd.DataFrame(data)

#duplicar linha
df.drop_duplicates(keep='last', inplace=True)

#calculando coluna 'preço do item'
df['preço do item'] = df['receita total']/df['quantidade de itens comprados']

#selecionar item acima de 50 reais
itens_acima_50 = df[df['preço do item'] > 50]

print('Itens acima de 50 reais:')
print(itens_acima_50)