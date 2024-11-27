informacoes = {}
for i in range(3):
    chave = input(f"Digite a chave {i + 1}: ")
    valor = input(f"Digite o valor para {chave}: ")
    informacoes[chave] = valor

print("Dicionário inserido:", informacoes)
