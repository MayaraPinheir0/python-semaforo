import time

#condicoes de trafego
fluxo_trafego = input("Digite o fluxo de tráfego (baixo, médio, alto): ").lower()

def verde():
    if fluxo_trafego == "baixo":
        print("Verde: 🟢 Fluxo baixo! Liberado por 3 segundos. ")
        time.sleep(3)
    elif fluxo_trafego == "medio":
        print("Verde: 🟢 Fluxo médio! Liberado por 5 segundos. ")
        time.sleep(5)
    else:
        print("Verde: 🟢 Fluxo alto! Liberado por 7 segundos. ")
        time.sleep(7)
        
def amarelo():
    if fluxo_trafego == "baixo":
        print("Amarelo: 🟡 Fluxo baixo! Espere por 1 segundo. ")
        time.sleep(1)
    elif fluxo_trafego == "medio":
        print("Amarelo: 🟡 Fluxo médio! Espere por 2 segundos. ")
        time.sleep(2)
    else:
        print("Amarelo: 🟡 Fluxo alto! Espere por 3 segundos. ")
        time.sleep(3)
        
def vermelho():
    if fluxo_trafego == "baixo":
        print("Vermelho: 🔴 Fluxo baixo! Espere por 1 segundo. ")
        time.sleep(1)
    elif fluxo_trafego == "medio":
        print("Vermelho: 🔴 Fluxo médio! Espere por 2 segundos. ")
        time.sleep(2)
    else:
        print("Vermelho: 🔴 Fluxo alto! Espere por 3 segundos. ")
        time.sleep(5)

while True:
    verde()
    amarelo()
    vermelho()