def contar_vogais(s):
    vogais = "aeiouAEIOU"
    count = sum(1 for char in s if char in vogais)
    return count

frase = input("Digite uma frase para contar as vogais: ")
resultado = contar_vogais(frase)
print(f"A quantidade de vogais na frase é {resultado}.")
