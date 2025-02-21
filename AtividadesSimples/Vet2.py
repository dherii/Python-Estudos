n=int(input('Quantos índices terá cada vetor? '))

a = [0] * n
b = [0] * n
c = [0] * n

print('Digite os valores do VETOR A :')
for i in range(0,n):
    a[i] = int(input())
print()


print('Digite os valores do VETOR B :')
for i in range(0,n):
    b[i] = int(input())
print()

print('SOMA VETORES A + B :')
for i in range(0,n):
    c[i] = a[i] + b[i]
    print(c[i])