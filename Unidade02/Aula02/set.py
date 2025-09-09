meu_conjunto=set()
print(f'Meu conjunto antes de adicionar: {meu_conjunto}')

#adicionando elementos
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)

print(f'Meu conjunto depois de adicionar: {meu_conjunto}')

#verificar um elemento no conjunto
elemento = 20

if elemento in meu_conjunto:
    print(f'{elemento} está no conjunto')
else:
    print(f'{elemento} não está no conjunto')

#removendo elemento do conjunto
meu_conjunto.remove(elemento)
print(f'Conjunto após remover {elemento}: {meu_conjunto}')