def media(lista):
    return sum(lista) / len(lista)

numeros = list(map(float, input("Digite números separados por espaço: ").split()))
resultado = media(numeros)
print(f"A média dos números fornecidos é {resultado:.2f}.")
