#pedir um numero até surgir um negativo, depois disso printar a soma e a média de todo o histórico e printar o primeiro

lista = []

while True:
    num = int(input())
    if num < 0:
        break
    elif num > -1:
        lista.append(num)
media = sum(lista) / len(lista)
lista.sort()
print(f"A soma de todos os números é: {sum(lista)}")
print(f"A media de todos os números é: {media}")
print(f"O menor de todos os números é: {lista[0]}")
