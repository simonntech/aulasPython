import pandas as pd

#dicionário com nomes e idades
dados = {
    'Nome':['Alice', 'Bruno', 'Clóvis', 'Mari', 'Jubercleide'],
    'Idade':[25,35,45,26,91]
}

serie_idades = pd.Series(dados['Idade'], index=dados['Nome'])

print('Série de Idades:')
print(serie_idades)

#média das idades
media_idades = serie_idades.mean()

print('\nMédia de Idades:', media_idades)