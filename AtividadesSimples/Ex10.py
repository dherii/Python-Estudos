n = int(input('Quantos números serão digitados? '))

for i in range (0, n):
    valor = int(input('Digite o número : '))
    if valor == 0:
        print ('Valor Nulo.')
    else:
        if valor % 2 == 0:
            print ('Par', end="")
        else:
            print('Ímpar', end="") 
        if valor > 0:
            print (' Positivo.')
        else:
            print(' Negativo.')
