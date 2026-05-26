#semáforo simples. Objetivo: criar um semáforo simples que alterna entre as cores verde, amarelo e vermelho, utilizando a função time.sleep() para controlar o tempo de cada cor.
import time

while True:
    print("  🚦   Semáforo em funcionamento...")
    print("Verde: 🟢")
    time.sleep(2)  # O semáforo fica verde por 2 segundos
    
    print("Amarelo: 🟡")
    time.sleep(1)  # O semáforo fica amarelo por 1 segundo

    print("Vermelho: 🔴")
    time.sleep(2)  # O semáforo fica vermelho por 2 segundos
    
# ao colocar o while True: e chamar as funções dentro do loop, o semáforo irá funcionar de forma contínua, alternando entre as cores verde, amarelo e vermelho.
# while é usado no final do codigo e nao no começo para evitar que o código entre em