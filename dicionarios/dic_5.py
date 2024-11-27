dias_da_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

numero = int(input("Digite um número de 1 a 7: "))
if 1 <= numero <= 7:
    print(f"O dia da semana correspondente é: {dias_da_semana[numero]}")
else:
    print("Número inválido. Digite um número entre 1 e 7.")
