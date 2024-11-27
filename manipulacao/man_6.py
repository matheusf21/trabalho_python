nome_arquivo = input("Digite o nome do arquivo: ")
texto = input("Digite o texto que deseja gravar: ")

with open(nome_arquivo, 'w') as file:
    file.write(texto)

print(f"Texto gravado no arquivo '{nome_arquivo}'.")
