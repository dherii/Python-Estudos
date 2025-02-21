import os

lista = []

while True:
   print('- Lista de Compras -')
   opcao = input('[i] inserir | [a] apagar | [l] listar: ')

   if opcao == 'i':
      os.system('cls')
      item = input('Item: ')
      lista.append(item)
   
   elif opcao == 'a':
      indice_str = input('Escolha o indicepara ser apagado: ')
      
      try:
         indice = int(indice_str)
         del lista[indice]
      except ValueError:
         print('Por favor, digite um número inteiro.')
      except IndexError:
         print('Índice inexistente.')
      except Exception:
         print('Erro desconhecido.')

   elif opcao == 'l':
      os.system('cls')
      
      if len(lista) == 0:
         print('Lista vazia. Nada para ser listado.')
      
      for i, item in enumerate(lista):
         print(i, item)