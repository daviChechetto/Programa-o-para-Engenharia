# Elabore um script em linguagem Python que leia de 10 números reais,
# inserindo-os numa lista e ao final, mostre-os na ordem inversa.

ns = []

for i in range(0,10):
    n = int(input())
    ns.append(n)

ns.reverse()

print(ns)