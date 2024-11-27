nota = float(input("Digite uma nota de 0 a 10: "))
if 0 <= nota <= 10:
    print(f"A nota {nota} é válida.")
else:
    print("Erro: A nota informada está fora do intervalo válido.")
