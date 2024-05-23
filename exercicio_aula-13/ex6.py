P1 = []
P2 = []

for i in range(0, 4):
    prova1 = float(input())
    P1.append(prova1)
    prova2 = float(input())
    P2.append(prova2)


media1 = sum(P1) / len(P1)
media2 = sum(P2) / len(P2)

print(f"Quantida de notas: {len(P1) + len(P2)}")

print(f"media da 1 prova: {media1}")
print(f"media da 2 prova: {media2}")

print(" media 1 maior") if media1 > media2 else print("media 2 maior")