from turtle import clear


print ('|1 - Álcool| ')
print ('|2 - Gasolina| ')
print ('|3 - Diesel| ')
print ('|4 - Finalizar Pedido|')

codigo = int(input('Digite o Código desejado : '))

alcool = 0
gasolina = 0
diesel = 0

while codigo != 4:
    if codigo == 1:
        alcool = alcool + 1
    elif codigo == 2:
        gasolina = gasolina + 1
    elif codigo == 3:
        diesel = diesel + 1
    
    print ('|1 - Álcool| ')
    print ('|2 - Gasolina| ')
    print ('|3 - Diesel| ')
    print ('|4 - Finalizar Pedido|')

    codigo = int(input('Digite o Código desejado : '))

print ('Pedido finalizado. Muito Obrigado!')
print ('Resumo do pedido : ')
print (f'Álcool : {alcool}L')
print (f'Gasolina : {gasolina}L')
print (f'Diesel : {diesel}L')
