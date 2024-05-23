dicionario = {"1" : ["maconha", 20, 3], 2 : ["metafetamina", 10, 2], 3 : ["cocaina", 5, 10], }
total =[]
for i in list(dicionario):
    precoUni = dicionario[i][1]  * dicionario[i][2]
    total.append(precoUni)
    print(precoUni)

print(f"TOTAL: {sum(total)}")