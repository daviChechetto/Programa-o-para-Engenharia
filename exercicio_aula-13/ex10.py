funcionarios = {1 : ["davi", "programador", 5], 2 : ["joa", "gay", 2]}

demitir = int(input())

if funcionarios[demitir][1] == "programador" and funcionarios[demitir][2] >= 3:
    print("escolha outro")
else:
    del funcionarios[demitir]
    
print(funcionarios)