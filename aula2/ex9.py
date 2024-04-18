valor = float(input("Digite o valor do produto: "))
descontos = input("0 - 0%\n1 - 10%\n2 - 20%\n3 - 30%\nDigite: ")

if descontos == "1":
    desconto = valor*0.9
    valorDescontado = valor*0.1
elif descontos == "2":
    desconto = valor*0.8
    valorDescontado = valor*0.2
elif descontos == "3":
    desconto = valor*0.7
    valorDescontado = valor*0.3
else:
    desconto = valor*1
    valorDescontado = valor*0

print("Preço inicial R${}\nVocê ganhou R${} de desconto\nValor Final R${}".format(valor,valorDescontado,desconto))