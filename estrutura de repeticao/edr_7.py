inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))
if inicio > fim:
    print("Erro: O início do intervalo não pode ser maior que o fim.")
else:
    print("Números pares no intervalo:")
    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            print(i)
