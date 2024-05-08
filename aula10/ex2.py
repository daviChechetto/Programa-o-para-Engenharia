""" 
Desenvolva um script em linguagem Python que peça as quatro notas de 10
alunos, calcule e armazene num vetor a média de cada aluno, imprima o
número de alunos com média maior ou igual a 7 """

notas = []
alunos = []


for i in range(0, 10):
    for i in range(0, 5):
        nota = float(input())
        notas.append(nota)
    media = sum(notas) / len(notas)
    if media >=7 : alunos.append(media)
    notas.clear()
    
print(len(alunos))