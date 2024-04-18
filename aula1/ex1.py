PV = float(input("Digite o Valor do investimento: "))
n = int(input("Digite o número de meses: "))
i = float(input("Digite a rentabilidade: "))

FV = PV*(1+i/100/12)**n
print("Montante final {:2f}".format(FV))