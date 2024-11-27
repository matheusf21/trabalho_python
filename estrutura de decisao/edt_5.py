num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

if operador == "+":
    resultado = num1 + num2
    print(f"O resultado da soma é {resultado}.")
elif operador == "-":
    resultado = num1 - num2
    print(f"O resultado da subtração é {resultado}.")
elif operador == "*":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é {resultado}.")
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é {resultado:.2f}.")
    else:
        print("Erro: Divisão por zero.")
else:
    print("Erro: Operador inválido.")
