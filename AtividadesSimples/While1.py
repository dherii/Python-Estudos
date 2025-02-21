idade = int(input('Digite a idade : '))

if idade < 0:
    print('Impossível calcular.')
else: 
    soma = 0
    nPessoas = 0
while idade >= 0:
    soma = soma + idade
    nPessoas = nPessoas + 1
    idade = int(input('Digite a idade : '))
media = soma / nPessoas
print (f'Quantidade de pessoas : {nPessoas}')
print (f'A média das idades é : {media:.2f}')