# Semaforo inteligente - Versão 3.0 
# Objetivo: criar um semáforo inteligente que se adapta ao fluxo de tráfego, utilizando sensores para detectar a presença de veículos e ajustar o tempo de cada sinal de acordo com a demanda. O semáforo inteligente pode ser implementado utilizando a biblioteca time para controlar o tempo de cada sinal, e a biblioteca os para limpar a tela e simular a presença de veículos.

#1. Importar a biblioteca time para controlar o tempo de cada sinal
import time
import os
from datetime import datetime

#2. Definir a função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
  
#3. Situação semáforo: verde
def verde():
    for i in range(tempo, 0, -1): # A função range(tempo, 0, -1) gera uma sequência de números começando em tempo, terminando antes de 0, e decrementando de 1 em 1.
        limpar_tela() # Chama a função limpar_tela() para limpar a tela antes de exibir a contagem regressiva.
        print("🟢 SEMÁFORO VERDE")
        print(f"Tempo restantes: 🟢 {i} segundos")
        time.sleep(1)
        
#4. Situação semáforo: amarelo
def amarelo():
    for i in range(3, 0, -1):
        limpar_tela()
        print("🟡 SEMÁFORO AMARELO")
        print(f"Tempo restantes: 🟡 {i} segundos")
        time.sleep(1)
        
#5. Situação semáforo: vermelho
def vermelho():
    for i in range(7, 0, -1):
        limpar_tela()
        print("🔴 SEMÁFORO VERMELHO")
        print(f"Tempo restantes: 🔴 {i} segundos")
        time.sleep(1)

#6. Situação semáforo: amarelo piscando
def amarelo_piscando():
    for i in range(10):
        limpar_tela()
        print("🟡 SEMÁFORO AMARELO")
        time.sleep(0.5)
        
        limpar_tela()
        print("⚫ SEMÁFORO APAGADO")
        time.sleep(0.5)

#7. Função para detectar veículos   
def detectar_veiculos():
    fluxo_veiculos = int(input("Digite o número de veículos detectados (0-100): "))
    return fluxo_veiculos

#8. Lógica principal 
def semaforo_inteligente():
    
    hora_atual = datetime.now().hour
    
    #8.1. madrugada
    if hora_atual >= 0 and hora_atual < 6:
        amarelo_piscando()
    
    else:
        
        fluxo_veiculos = detectar_veiculos()
        
        # 8.2. fluxo alto
        if fluxo_veiculos > 50:
            verde(10)  # O semáforo fica verde por 10 segundos
        
        # 8.3. fluxo normal
        else:
            verde(5)  # O semáforo fica verde por 5 segundos
            
        amarelo(2)
        vermelho(5)

#9. Programa principal
while True:
    semaforo_inteligente()