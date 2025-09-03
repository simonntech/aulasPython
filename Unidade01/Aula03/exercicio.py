filmes = ["A volta dos que não foram", "Longas tranças de um careca", "Super Fighter", "Não vingativos", "Lindomar Voador"]

print()
print()
print()

for filme in filmes:
    while True:
        classificacao = input(f"{filme} de 1 a 5? (ou 0 para parar):")
        if classificacao == '0':
            print(f"{filme} interrompida.")
            break
        classificacao = int(classificacao)
        if classificacao <1 or classificacao>5:
            print()
        else:
            print(f"{filme} com {classificacao} estrelas. \n")
            break

print()