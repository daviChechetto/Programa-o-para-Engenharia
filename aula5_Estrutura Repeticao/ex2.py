#printar os números primos

numero = int(input())
i=0
indice = 0
for i in range(numero, 0, -1):
    if numero%i == 0:
        indice +=1

print("primo") if indice == 2 else print(f"O número: {numero} não é primo")   