import csv

try:
    with open('dados.csv', 'r') as file:
        leitor = csv.reader(file)
        for linha in leitor:
            print("\t".join(linha))
except FileNotFoundError:
    print("Erro: O arquivo 'dados.csv' não foi encontrado.")
