soma = 0
while True:
    num = int(input("Digite um número (ou 0 para sair): "))
    if num == 0:
        break
    soma += num
print(f"A soma dos números digitados é {soma}.")
