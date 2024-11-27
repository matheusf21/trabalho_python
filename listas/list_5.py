entrada = input("Digite números inteiros separados por espaço: ")
numeros = list(map(int, entrada.split()))
soma = sum(numeros)
print(f"Soma dos elementos da lista: {soma}")
