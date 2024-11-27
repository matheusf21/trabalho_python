# Solicitar dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizar as operações
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Verificar se a divisão é possível
if num2 != 0:
    divisao = num1 / num2
    print(f"A divisão do primeiro número pelo segundo é {divisao:.2f}.")
else:
    print("A divisão por zero não é possível.")

# Exibir os resultados
print(f"A soma dos números é {soma}.")
print(f"A subtração do primeiro número pelo segundo é {subtracao}.")
print(f"A multiplicação dos números é {multiplicacao}.")
