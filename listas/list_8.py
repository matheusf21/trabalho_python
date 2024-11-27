entrada = input("Digite palavras separadas por espaço: ")
palavras = entrada.split()
busca = input("Digite a palavra a ser buscada: ")
if busca in palavras:
    print(f"A palavra '{busca}' está na lista.")
else:
    print(f"A palavra '{busca}' não está na lista.")
