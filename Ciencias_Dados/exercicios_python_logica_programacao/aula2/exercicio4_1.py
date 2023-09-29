'''
A trajetória balística obedece às equações de lançamento oblíquo. O projétil a ser lançado deve ser 
posicionado formando um ângulo (q) com o solo e ser disparado com uma velocidade inicial (V0) .
Os cálculos da trajetória na horizontal (x) e vertical (y - altura) podem ser realizados aplicando-se 
o tempo nas equações a seguir:

'''

#tentei fazer em vpython, mas nao consegui achar a altura, deu diferença nos valores do ângulo em python e no vpython, então acho que eu não soube achar o ângulo correto.

from vpython import *

#objeto
bola = sphere(pos = vector(0,0,0), radius = 0.7, color = color.blue, make_trail = True)


#condição inicial
v0 = (100/(0.83**2))
theta = 45*(pi/180)
g = vector(0,-10,0)
bola.v = vector(v0*cos(theta), v0*sin(theta),0)

t = 0
dt = 0.001

#equação do movimento
while bola.pos.y >= 0:
  rate(500)
  
  bola.v = bola.v + g*dt
  bola.pos = bola.pos + bola.v*dt
  
 
  t = t + dt
  
  
print('O tempo de voo da bola foi: ', round(t,2), 's')
print('O alcance da bola foi: ', round(bola.pos.x,2), 'm')