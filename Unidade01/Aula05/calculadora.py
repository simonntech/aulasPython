valorProduto = float(input("Digite o valor do produto: R$ "))
percentualDesconto = float(input("Qual o percentual do desconto? "))

if percentualDesconto < 0 or percentualDesconto > 100:
    print("O valor do desconto deve ser entre 0% a 100%")
else:
    desconto = valorProduto * (percentualDesconto / 100)
    valorFinal = valorProduto - desconto
    print(f"Valor com desconto: R$ {valorFinal:.2f}")