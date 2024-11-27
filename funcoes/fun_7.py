def calcular_preco_final(preco, desconto):
    return preco - (preco * (desconto / 100))

preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))

preco_final = calcular_preco_final(preco, desconto)
print(f"O preço final com {desconto}% de desconto é R$ {preco_final:.2f}.")
