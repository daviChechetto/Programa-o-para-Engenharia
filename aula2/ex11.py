import math

diametro = float(input("Digite o diametro do cano (em metros): "))
tempo = float(input("Digite a tempo do fluxo (em m/s): "))

tamanho = 1
volume = (diametro/2)**2 * math.pi * tamanho
vazao = volume / tempo

print(vazao)