import os
import platform

def limpar_terminal():
    # Verifica o sistema operacional
    if platform.system() == "Windows":
        os.system("cls")  # Comando para Windows
    else:
        os.system("clear")  # Comando para Linux ou macOS


while True:
   n1 = input("Informe o primeiro valor: ")
   n2 = input("Informe o segundo valor: ")

   try:
      n1_float = float(n1)
      n2_float = float(n2)
   except ValueError:
      print('Um ou mais números digitados são inválidos.')

   operador = input("Qual será o sinal de opereação? [ + | - | x | / ] ")
   if operador == '+':
      resultado = n1_float + n2_float
   elif operador == '-':
         resultado = n1_float - n2_float
   elif operador == 'x':
         resultado = n1_float * n2_float
   elif operador == '/':
      if n2_float == 0:
         print('Erro: Divisão por zero.')
         continue
      resultado = n1_float / n2_float
   else:
      print('Operador Inválido.')   
      
   print(f'Resultado : {resultado}')

   sair = input("Deseja sair? [s]im ").lower().startswith('s')

   limpar_terminal()
   if sair:
      break

print('Calculadora encerrada.')