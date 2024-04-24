# Pegar 5 numeros e mostrar a lista invertida

inteiros = []

for i in range(5):
    numero = int(input())
    inteiros.append(numero)

inteiros.reverse()

print(inteiros)