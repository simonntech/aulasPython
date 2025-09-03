print("Média de notas semestrais:")
print("--------------------------")

name = input("Nome do(a) Aluno: ")
notes = []

for i in range (4):
    bim = i+1

    while True:
        try: 
            note = float(input(f"Nota do {bim}º bimestre: "))
            if 0<=note <=10:
                break
            else: 
                print("Por favor, digite uma nota válida entre 0 a 10")
        except ValueError:
            print("Digite uma nota válida com números, entre 0 a 10")
            
    notes.append(note)

media = sum(notes)/len(notes)

if media >= 7:
    situacao = 'aprovado! ✔'
else:
    situacao= 'reprovado... ❌'

print("------------- RESULTADO FINAL")
print(f"As notas do(a) aluno(a): {name} foram: {notes}")
print(f"A média final foi: {media}, e está {situacao}")