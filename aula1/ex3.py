copias = int(input("Digite o número de cópias: "))
vTotal = copias*(24.95-(24.95*0.35)) + 3 + (0.75*(copias-1))
print("O valor total é de: {}".format(vTotal))