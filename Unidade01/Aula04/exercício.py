notas = [7.5, 5.0, 6.5, 7.0, 7.0]

def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

arredondar_media = lambda media: round(media, 2)

media = calcular_media(notas)
media_arredondada = arredondar_media(media)

if media_arredondada >=7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'


print(f"As notas do aluno foram: {notas}")
print(f"Sua média arredonda foi {media_arredondada}")
print(f"Está {situacao}")