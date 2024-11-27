try:
    with open('diario.txt', 'a') as file:
        entrada = input("Digite a nova entrada para o diário: ")
        file.write(entrada + "\n")
    print("Nova entrada adicionada ao 'diario.txt'.")
except FileNotFoundError:
    with open('diario.txt', 'w') as file:
        entrada = input("Digite a primeira entrada para o diário: ")
        file.write(entrada + "\n")
    print("Arquivo 'diario.txt' criado e primeira entrada adicionada.")
