entrada = input("Digite números separados por espaço: ")
numeros = list(map(int, entrada.split()))
print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")
