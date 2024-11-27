print("Digite 5 números para a primeira lista:")
lista1 = [int(input(f"Digite o {i + 1}º número: ")) for i in range(5)]

print("Digite 5 números para a segunda lista:")
lista2 = [int(input(f"Digite o {i + 1}º número: ")) for i in range(5)]

somas = [a + b for a, b in zip(lista1, lista2)]
print("Lista com as somas dos elementos correspondentes:", somas)
