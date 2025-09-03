#funções built in
numeros = [1, 2, 3, 4, 5, 6]

comprimento = len(numeros) #len é uma função built in

print(f"Tamanho do array: {comprimento}")

#funções definidas: DEF

def soma(a,b):
    resultado = a+ b
    return resultado

resultado_soma = soma(10,80)

print(f"O resultado da soma é {resultado_soma}")

#outra função def
def e_par(numero):
    if numero %2 ==0:
        return 'Par'
    else:
        return 'Ímpar'
    
print(f"O número 10 é {e_par(10)}")