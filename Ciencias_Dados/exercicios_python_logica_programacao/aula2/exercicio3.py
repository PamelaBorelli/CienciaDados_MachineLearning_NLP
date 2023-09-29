'''

O teste principal consiste em segmentar a pista em 4 partes e efetuar alguns cálculos de velocidade e aceleração. O comprimento de cada parte não é fixo, variando de acordo com os protocolos de ensaios.

Você foi contratado para o desenvolvimento de um algoritmo e efetuar a implementação em 
Python, do software para monitoramentos de parâmetros de movimento cinemático dos veículos 
trafegando pelo circuito:

a)) Efetuar a leitura da distância e o tempo de percurso de 
cada trecho.
b) Calcular a velocidade média de cada trecho.
c) Calcular a velocidade média total.
d) Calcular a aceleração entre dois trechos consecutivos

'''

import os


n = 4
distancias = [0] * n
tempos = [0] * n

# Pergunta ao usuário as distâncias e tempos percorridos em cada segmento
for i in range(n):
    distancias[i] = float(input(f'Digite a distância percorrida no trecho {i + 1} (em km): '))
    tempos[i] = float(input(f'Digite o tempo gasto para percorrer o trecho {i + 1} (em horas): '))

os.system("cls")

velocidades = [0] * n
aceleracoes = [0] * (n - 1)
aceleracoesTrechos = [0] * (n - 2)

for i in range(n):
    # Calcula a velocidade do trecho i
    velocidades[i] = distancias[i] / tempos[i]

    if i > 0:
        # Calcula a aceleração do trecho i
        aceleracoes[i - 1] = (velocidades[i] - velocidades[i - 1]) / tempos[i]

        if i > 1:
            # Calcula a aceleração entre os trechos i-1 e i
            aceleracoesTrechos[i - 2] = (aceleracoes[i - 1] - aceleracoes[i - 2]) / tempos[i]

# Calcula a velocidade média total
distanciaTotal = sum(distancias)
tempoTotal = sum(tempos)
velocidadeMedia = distanciaTotal / tempoTotal

print(f'Velocidades de cada trecho: {velocidades}')
print(f'Velocidade média total: {velocidadeMedia}')
print(f'Acelerações entre trechos: {aceleracoesTrechos}')


