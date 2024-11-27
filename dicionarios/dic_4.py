pessoas = {
    "João": 25,
    "Maria": 30,
    "Pedro": 22
}

nome = input("Digite o nome a ser verificado: ")

if nome in pessoas:
    print(f"O nome {nome} foi encontrado!")
else:
    print(f"O nome {nome} não foi encontrado!")
