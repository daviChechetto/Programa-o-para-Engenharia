""" ----------------------------------------- 

a = 10
b = 20
soma = a + b
print(soma)

----------------------------------------- 

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))

soma2 = n1 + n2 + n3

print("A soma dos 3 n° é: {}".format(soma2))

----------------------------------------- 

v1 = int(input("Digite 1° n: "))
v2 = int(input("Digite 2° n: "))
mult = v1 * v2 
print("a multipicação é de: {}".format(mult))

-----------------------------------------   

nu1 = float(input("Digite o dividendo: "))
nu2 = float(input("Digite o divisor: "))
div = nu1 / nu2
print("A divisão é de: {}".format(div))

----------------------------------------- 

x=1
while x == 1:
    a = float(input("Digite o dividendo: "))
    b = float(input("Digite o divisor DIFERENTE de 0: "))

    try:
        print(a/b)
    except ZeroDivisionError:
        print("n dá, o divisor é 0 burrao pra krl")
        x = 2
        break
    
    print("vamos dnv")

print("jdnfgjin")

----------------------------------------- """

prova1 = float(input("Digite a primeira nota: "))
prova2 = float(input("Digite a segunda nota: "))
media = (prova1+prova2)/2
print("A sua media é de: {}".format(media))
if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")