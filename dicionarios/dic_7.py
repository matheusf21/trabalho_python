precos = {
    "Arroz": 20.5,
    "Feijão": 7.8,
    "Carne": 25.0,
    "Leite": 3.2,
    "Pão": 2.5
}

produto = input("Digite o nome do produto: ")

if produto in precos:
    print(f"O preço do {produto} é: R$ {precos[produto]:.2f}")
else:
    print("Produto não encontrado.")
