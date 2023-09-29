'''
A trajetória balística obedece às equações de lançamento oblíquo. O projétil a ser lançado deve ser 
posicionado formando um ângulo (q) com o solo e ser disparado com uma velocidade inicial (V0) .
Os cálculos da trajetória na horizontal (x) e vertical (y - altura) podem ser realizados aplicando-se 
o tempo nas equações a seguir:

'''

import math
from math import *


#entrada de dados
v0 = 100/0.83
theta = 55
g=9.8


#processamento e dados de saída

# Converte o ângulo de graus para radianos (tentei de duas maneiras, não estou certa sobre o ângulo)
# angulo = math.radians(theta)
angulo = theta*pi/180

# Calcula a velocidade inicial em x e y
velocidadeX = v0 * math.cos(angulo)
velocidadeY = v0 * math.sin(angulo)


# Calcula o tempo de voo
tempo = 2 * velocidadeY / g
print(f'Tempo de voo: {tempo}')

# Calcula a distância percorrida
distancia = velocidadeX * tempo
print(f'Distancia percorrida: {distancia}')

# Calcula a altura máxima atingida
altura= (velocidadeY ** 2) / (2 * g)
print(f'Altura máxima: {altura}')




