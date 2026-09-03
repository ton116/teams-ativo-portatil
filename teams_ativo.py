import pyautogui
import time
from datetime import datetime

# Trava de segurança ativada
pyautogui.FAILSAFE = True

# Tempo de intervalo em segundos (2 minutos)
INTERVALO_SEGUNDOS = 10

print("==================================================")
print(" KeepAlive Teams Initiated")
print(f" Simulando atividade a cada {INTERVALO_SEGUNDOS} segundos.")
print(" Nenhuma janela ou texto será digitado.")
print(" Para PARAR: Pressione Ctrl + C no terminal.")
print("==================================================")

contador = 1

try:
    while True:
        hora_atual = datetime.now().strftime("%H:%M:%S")

        # Pega a posição atual exata do seu mouse
        x, y = pyautogui.position()

        # Move o mouse 1 pixel para a direita e retorna imediatamente
        pyautogui.moveTo(x + 1, y)
        pyautogui.moveTo(x, y)

        print(f"[{hora_atual}] -> Pulso #{contador} enviado. Teams ativo! (Próximo em {INTERVALO_SEGUNDOS}s)")

        contador += 1
        time.sleep(INTERVALO_SEGUNDOS)

except KeyboardInterrupt:
    print("\nScript encerrado com sucesso!")