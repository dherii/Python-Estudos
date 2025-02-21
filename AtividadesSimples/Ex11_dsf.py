tests = int(input("Quantos casos serão analisados? "))
R=0
C=0
S=0
Qcob=0
for i in range(0,tests):
    Qcob = int(input("Quantidade de cobaias? "))
    print("Tipos : R - Ratos | C - Coelhos | S - Sapos")
    tipo=input("Tipo de cobaia: ") 

    if tipo=="R":
        R=R+Qcob
    elif tipo=="C":
        C=C+Qcob
    else:
        S=S+Qcob
Tcob=R+C+S
pR=(R/Tcob)*100
pC=(C/Tcob)*100
pS=(S/Tcob)*100
print()

print("RELATÓRIO FINAL :")
print()
print(f"Total de Cobaias : ",Tcob)
print(f"Quantidade de Ratos : ", R)
print(f'Quantidade de Coelhos : ', C)
print(f'Quantidade de Sapos : ',S)
print()
print(f'Porcentagem de Ratos : {pR}%')
print(f'Porcentagem de Coelhos : {pC}%')
print(f'Porcentagem de Sapos : {pS}%')