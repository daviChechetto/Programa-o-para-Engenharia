medias = []

for i in range(0,4):

    notas = []
    for i in range(0, 3):
        nota = float(input("nota: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias.append(media)
    print(media)

print(medias)

passou = 0
for i in list(medias):
    
    if i >= 7:
        passou += 1
    else:
        continue
print(f"Apenas passaram {passou} pessoas")