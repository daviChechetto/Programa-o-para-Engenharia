# uma espécie de roleta com 10 chances

from random import randint

maximo = 10
tentativas = 0
num_sorteado = randint(0,100)
num = 0

while (tentativas < maximo) and (num != num_sorteado):
    print(f"Você tem {tentativas} de {maximo} chances!")
    num = int(input("Digite um número: "))
    if num > num_sorteado:
        print(f"O número sorteado é menor que: {num}")
    elif num < num_sorteado:
        print(f"O número sorteado é maior que: {num}")
    tentativas += 1
if num == num_sorteado:
    print(f"parabéns, você acertou com apenas {tentativas}")
else:
    print("não foi dessa vez!")