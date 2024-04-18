valor = float(input("Digite o valor do produto: "))

desconto = valor*0.8
valorDescontado = valor*0.2
print("Preço inicial R${}\nVocê ganhou R${} de desconto\nValor Final R${}".format(valor,valorDescontado,desconto))