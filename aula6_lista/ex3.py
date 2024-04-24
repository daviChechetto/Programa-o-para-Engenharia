lista = []

for i in range(3):
    nota = float(input())
    lista.append(nota)

lista.sort()
print(f"nota mais alta: {lista[2]}, nota mais baixa: {lista[0]} e a média: {sum(lista)/3}")