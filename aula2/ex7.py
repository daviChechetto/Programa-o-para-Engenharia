gasto = float(input("Quanto você vai gastar de combstível: "))

litros = gasto/4.95
quilometragem = litros * 20

print("Você irá comprar {} litro(s) de combustível e irá andar {} Km".format(litros,quilometragem))