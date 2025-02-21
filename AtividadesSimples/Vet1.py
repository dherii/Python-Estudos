N=int(input("Quantidade de números que serão digitados : "))
print()
vet = [0] * N

for i in range (0,N):
    vet[i] = int(input("Digite um número : "))
print()
print("NÚMEROS PARES :")
Qpar = 0
for i in range (0,N):
    if vet[i]%2==0:
        print(f'{vet[i]}')
        Qpar= Qpar + 1
print()
print(f"QUANTIDADE DE PARES : {Qpar} ")

    


