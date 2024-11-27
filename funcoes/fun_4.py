def maior(a, b, c):
    return max(a, b, c)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

resultado = maior(num1, num2, num3)
print(f"O maior número entre {num1}, {num2} e {num3} é {resultado}.")
