lista = []
pares = []

for i in range(0,4):
    n = int(input())
    lista.append(n)

for i in list(lista):
    if i % 2:
        par = lista[i]
        pares.append(par)

print(pares)