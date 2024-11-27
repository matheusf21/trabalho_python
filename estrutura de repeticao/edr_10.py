num = int(input("Digite um número inteiro positivo: "))
if num > 1:
    eh_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")
else:
    print("Erro: O número deve ser maior que 1.")
