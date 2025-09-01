nota_1 = int(input("Primeira nota: "))
nota_2 = int(input("Segunda nota: "))
nota_3 = int(input("Terceira nota: "))
nota_4 = int(input("Quarta nota: "))

media = (nota_1 + nota_2 + nota_3 + nota_4)/4

if media >= 6:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

print(f"Nota final: {media}")
print(f"Aluno {situacao}")