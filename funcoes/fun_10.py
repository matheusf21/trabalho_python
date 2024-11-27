def tabuada(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

numero = int(input("Digite um número para ver a tabuada: "))
tabuada(numero)
