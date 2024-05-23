Vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)

media = sum(Vendas) / len(Vendas)

variancia =  sum((x - media) ** 2 for x in Vendas)

print(f"Media: {media :.2f}")

print(f"Variancia: {variancia :.2f}")

print(f"Desvio padrão: √{variancia :.2f}")