convidados = ('Alice', 'Bob', 'Carol', 'David', 'Eve')

confirmados = ['Bob', 'David']

nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

print('Convidados que ainda não confirmaram:')

for pessoa in nao_confirmados:
    print(pessoa)

print('\nEnviando lembretes para os convidados que ainda não confirmaram...')