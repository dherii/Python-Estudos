import pyautogui # type: ignore
import time

# Tempo de espera em segundos
tempo_espera = 9.6  # Ajuste para o tempo desejado
time.sleep(5)
coordenadas = pyautogui.position()
# Coordenadas do canto da tela onde deseja clicar
#coordenadas = (862, 635)  # Ajuste para as coordenadas desejadas

repeticoes = 50
for i in range(repeticoes):
   # Realiza o clique
   pyautogui.click(x=coordenadas[0], y=coordenadas[1])
   print(i)

   time.sleep(tempo_espera)

print('Loop finalizado.')
