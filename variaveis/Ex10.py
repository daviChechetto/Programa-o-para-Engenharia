import math


x1 = int(input("digite o X do Ponto1: "))
y1 = int(input("digite o Y do Ponto1: "))

x2 = int(input("digite o X do Ponto2: "))
y2 = int(input("digite o Y do Ponto2: "))

d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(d)