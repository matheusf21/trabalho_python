produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade comprada: "))
preco_unitario = float(input("Digite o preço unitário do produto: "))
total = quantidade * preco_unitario
print(f"O valor total da compra do produto {produto} é R${total:.2f}.")
