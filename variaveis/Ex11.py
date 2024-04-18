corretor = input("Digite o nome do corretor: ")
imoveis_vendidos = int(input("digite o número de imóveis vendidos: "))
valor_total = float(input("Digite o valor total de suas vendas: "))

salario = 1500 + imoveis_vendidos*200 + valor_total*0.05

print(salario)