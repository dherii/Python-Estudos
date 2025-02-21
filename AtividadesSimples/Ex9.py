N=int(input("Digite um valor para N : "))

fatorial=1

for i in range(N,0,-1):
    fatorial=fatorial * i

print(f"FATORIAL :", fatorial)
