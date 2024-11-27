alunos = {}
for i in range(5):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

for nome, nota in alunos.items():
    print(f"Aluno: {nome}, Nota: {nota}")
