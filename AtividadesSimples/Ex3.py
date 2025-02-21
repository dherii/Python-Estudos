print("- MINI CALCULADORA -")
print()
print (" x =< 5 então x * 10")
print (" x > 5 e x =< 10 então x * 20")
print (" x >= 11 então x + 100")
print()
x = int(input("Digite um valor : "))

if x <= 5:
    resultado = x * 5
elif x >= 6 and x <=10:
    resultado = x * 20
elif x >= 11:
    resultado = x + 100

print (f"R : {resultado}")