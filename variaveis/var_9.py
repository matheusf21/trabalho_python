dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

total_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print(f"O total de segundos é {total_segundos}.")
