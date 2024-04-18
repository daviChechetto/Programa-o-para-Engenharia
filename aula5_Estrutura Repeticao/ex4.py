#calculadora

while True:
    n1 = float(input())
    print(" 1 - adição\n 2 - subtração\n 3 - multiplicação\n 4 - divisão\n 5 - sair")
    opcao = int(input())
    n2 = float(input())

    if opcao == 1:
        print(n1+n2)
    elif opcao == 2:
        print(n1-n2)
    elif opcao == 3:
        print(n1*n2)
    elif opcao == 4:
        print(n1/n2)
    else:
        break
