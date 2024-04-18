import math

raio = float(input("Digite o raio: "))

perimetro = 2 * math.pi * raio 
area = math.pi * raio**2

print("Perimetro: {:2f}\nArea: {:2f}".format(perimetro, area))
