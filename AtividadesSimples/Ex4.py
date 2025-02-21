print("- COMPARADOR DE VALORES -")
valor1 = int(input("Digite o primeiro valor : "))
valor2 = int(input("Digite o segundo valor : "))
valor3 = int(input("Digite o terceiro valor : "))

MaxV = valor1
MinV = valor1
#MAIOR VALOR 
if valor2>valor1:
    MaxV = valor2
if valor3>valor2:
    MaxV = valor3

#MENOR VALOR
if valor2<valor1:
    MinV = valor2
if valor3<valor2:
    MinV = valor3

print (f"Maior Valor : {MaxV}")
print(f"Menor Valor : {MinV}")