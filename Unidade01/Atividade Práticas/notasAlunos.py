print("Média de notas semestrais:")
print("--------------------------")

#implementada uma variável para armazenar o nome do(a) aluno(a)
name = input("Nome do(a) Aluno: ")

#foi criado um array vazio antes do escopo do laço de repetição, para depois serem adicionadas as notas 
notes = []

#laço de repetição FOR com a quantidade de notas 
for i in range (4):

#a variável "prove" recebe "i"+1 devido o valor de repetição iniciar em 0
    prove = i+1

#laço de validação com WHILE
    while True:

#validação com TRY e EXCEPT implementados para validar se o usuário digita um número ou string
        try: 
            # o valor da nota digitado pelo usuário é inserida na variável note
            note = float(input(f"Nota da {prove}ª prova: "))
            #se a variável for entre 1 a 10, o laço do WHILE se quebra
            if 0<=note <=10:
                break
            else: 
                print("Por favor, digite uma nota válida entre 0 a 10")
        except ValueError:
            print("Digite uma nota válida com números, entre 0 a 10")

#cada nota será anexada no array "notes" em cada interação do "i" no laço FOR
    notes.append(note)

#cálculo da média das notas, usando as funções do Python "sum()" para somar todos os valores do array NOTES, e "len()" para calcular o tamanho do array e usar no cálculo da média
media = sum(notes)/len(notes)

#condições para ser aprovado ou não
if media >= 7:
    situacao = 'aprovado! ✔'
else:
    situacao= 'reprovado... ❌'

#saídas finais da situação do(a) aluno(a), com o nome, as notas e aprovação
print("------------- RESULTADO FINAL")
print(f"As notas do(a) aluno(a): {name} foram: {notes}")
print(f"A média final foi: {media}, e está {situacao}")