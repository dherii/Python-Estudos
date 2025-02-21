n = int(input('Quantos números serão digitados? '))
dentro = 0
fora = 0
print()
for i in range(1,n+1):
    x = int(input('Digite um número :'))
    if x>=10 and x<=20:
        dentro = dentro + 1
    else:
        fora = fora + 1
print ()
print (f'Dentro do Intervalo : {dentro}')
print (f'Fora do Intervalo : {fora}')
