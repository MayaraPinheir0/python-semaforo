# 1. Evolução do projeto 

Nível 1 — Básico
print
loops
sleep
variáveis

Nível 2 — Intermediário
funções
módulos
contagem regressiva

Nível 3 — Lógica
condições
sensores
pedestres

Nível 4 — Visual
interface gráfica
animações

Nível 5 — Avançado
múltiplos cruzamentos
sincronização
orientação a objetos

Próximo passo recomendado
Semáforo básico
Semáforo com contagem
Semáforo gráfico
Cruzamento com 2 semáforos
Simulação de trânsito simples# python-semaforo


# 2. para me ajudar a como pensar em abstracao 

Sempre faça estas perguntas:
1. O que existe no mundo real?
Exemplo:

semáforo
carros
sensores
horário

2. O que precisa acontecer?

Exemplo:

trocar sinal
esperar
detectar carros
mudar comportamento

3. O que pode virar variável?

exemplo:

fluxo
hora
tempo_verde

4. O que pode virar função?

Exemplo:

verde()
amarelo()
vermelho()

5. O que é decisão?

Exemplo:

if fluxo > 50

# PARA FIXAR
# A. Analisar o evento/ objeto
Escolha algo simples (ex. elevador, ventilador etc.) e pergunte-se:

* O que ele possui?
* O que ele faz?
* Quais decisões ele toma?

geralmente abstracao há variaveis, funções e decisões

# B. Desenhe antes de programar

``` flowchart TD
INÍCIO
 ↓
verificar hora
 ↓
é madrugada?
 ↓
sim → amarelo piscando
não
 ↓
verificar fluxo
 ↓
alto?
 ↓
verde maior
 ↓
amarelo
 ↓
vermelho
```

# C. Explicar o que o código faz em linguagem natural
# D. Realizar pequenas modificaçoes
Tente:

mudar tempos
inverter lógica
criar novo modo
adicionar mensagens
quebrar algo e corrigir

* Programadores aprendem MUITO errando.