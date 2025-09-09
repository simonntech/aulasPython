#dicionários dict

#exemplo 1 de como criar atribuição
dici_1 = {}
dici_1['nome'] = 'Brunão'
dici_1['idade']= 35
print(dici_1)

#exemplo 2 de como criar atribuição
dici_2 = {
    'nome': 'Mariana', 
    'idade': 27
    }
print(dici_2)

#exemplo 3 - dicionário com uma lista de tuplas
dici_3 = dict([
    ('nome', 'Maria'), 
    ('idade', 18)
    ])
print(dici_3)

#exemplo 4 - usando zip
dici_4 = dict(zip(
    ['nome', 'idade'], 
    ['Mario', 100]
    ))
print(dici_4)

#verificar tipo de dados - class DICT
print(type(dici_1)==type(dici_2)==type(dici_3)==type(dici_4))
print(type(dici_1))