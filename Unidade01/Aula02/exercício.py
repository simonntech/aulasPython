print("Bem vindo à Máquina de Venda Automática de Ingressos de Cinema!")

idade = int(input("Por favor, digite sua idade: "))

if idade < 12:
    print ("Recomendamos filmes infantis 🧑👧")
elif 12 <= idade < 18 :
    print ("Recomendamos filmes adolescentes 👱‍♂️👱‍♀️")
else:
    print ("Recomendamos filmes adultos 🧔👩‍🦰")

quantidade_ingressos = 10

if quantidade_ingressos > 0:
    print("Ingressos disponíveis.")
else:
    print ("Ingressos esgotados...")