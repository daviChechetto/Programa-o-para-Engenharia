numeros = []

while True:
    numero = int(input())
    if numero >= 0:
        numeros.append(numero)
    else:
        break

soma = sum(numeros)
media = soma / len(numeros)
print(soma, " : soma")
print(media, " : media")
print(max(numeros), " : maior")
print(min(numeros), " : menor")