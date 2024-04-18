import math

raio1 = float(input("Digite raio 1: "))
raio2 = float(input("Digite raio 2: "))


area1 = math.pi * raio1**2
area2 = math.pi * raio2**2

anel = area1 - area2

print(anel)