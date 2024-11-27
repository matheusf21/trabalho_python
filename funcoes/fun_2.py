def é_par(numero):
    return numero % 2 == 0

num = int(input("Digite um número para verificar se é par: "))

if é_par(num):
    print(f"{num} é um número par.")
else:
    print(f"{num} não é um número par.")
