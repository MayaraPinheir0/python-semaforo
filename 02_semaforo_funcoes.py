# Semáforo com funções. 
# Objetivo: criar um semáforo mais organizado e modular, utilizando funções para cada cor do semáforo. Isso torna o código mais legível e fácil de manter.

#1. Importar as bibliotecas
import time
import os # Importa a biblioteca os para limpar a tela

#2. Definir a funçao para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt'else 'clear') # os.system é usado para executar um comando do sistema operacional. 'cls' é o comando para limpar a tela no Windows, enquanto 'clear' é o comando para limpar a tela em sistemas Unix/Linux/Mac. A expressão 'cls' if os.name == 'nt' else 'clear' verifica o sistema operacional e escolhe o comando apropriado.

#3. Definir a funções do sinal verde, amarelo e vermelho
def verde():
    for i in range(10, 0, -1): # A função range(10, 0, -1) gera uma sequência de números começando em 10, terminando antes de 0, e decrementando de 1 em 1.
        limpar_tela() # Chama a função limpar_tela() para limpar a tela antes de exibir a contagem regressiva.
        print("🟢 SEMÁFORO VERDE")
        print(f"Tempo restantes: 🟢 {i} segundos")
        print("🚗 Carros podem passar")
        time.sleep(1)

def amarelo():
    for i in range(3, 0, -1):
        limpar_tela()
        print("🟡 SEMÁFORO AMARELO")
        print(f"Tempo restantes: 🟡 {i} segundos")
        time.sleep(1)

def vermelho():
    for i in range(7, 0, -1):
        limpar_tela()
        print("🔴 SEMÁFORO VERMELHO")
        print(f"Tempo restantes: 🔴 {i} segundos")
        time.sleep(1)


#4. Criar um loop para chamar as funções em sequência   
while True:
    verde()
    amarelo()
    vermelho()

# ao colocar o while True: e chamar as funções dentro do loop, o semáforo irá funcionar de forma contínua, alternando entre as cores verde, amarelo e vermelho.
# while é usado no final do codigo e nao no começo para evitar que o código entre em um loop infinito antes de definir as funções. Dessa forma, as funções são definidas primeiro e depois o loop é iniciado para chamar as funções repetidamente.