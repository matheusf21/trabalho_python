notas = {}
for i in range(4):
    disciplina = input(f"Digite o nome da {i + 1}ª disciplina: ")
    nota = float(input(f"Digite a nota de {disciplina}: "))
    notas[disciplina] = nota

media = sum(notas.values()) / len(notas)
print(f"Média das notas: {media:.2f}")
