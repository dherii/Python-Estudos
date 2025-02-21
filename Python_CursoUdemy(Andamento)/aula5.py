"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num_str = input("Informe um número inteiro: ")

try:
   num_int = int(num_str)
   if num_int % 2 == 0:
      print('O número digitado é PAR.')
   else:
      print('O número digitado é ÍMPAR.')
except:
   print('O número/caractere digitado não é inteiro.')
