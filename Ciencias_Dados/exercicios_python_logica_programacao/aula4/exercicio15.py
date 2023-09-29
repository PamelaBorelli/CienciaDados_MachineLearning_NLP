'''
Utilizando o código do exercício anterior, efetue alterações para evitar exceções no processamento caso o jogador digite uma opção inválida.

'''
from random import randint
import random


#entrada de dados


itens = ('Pedra', 'Papel', 'Tesoura')
# computador = randint(0,2)
computador=int(random.randint(0,301)/100)
print('''Escolha um opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input("Qual a sua opção: "))

#dados de saída
print("O computador escolheu   ==> {}".format(itens[computador]))
print("O você escolheu         ==> {}".format(itens[jogador]))


#processamento
if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("VOCÊ VENCEU")
    elif jogador == 2:
        print("O COMPUTADOR VENCEU")
    elif jogador>= 3: 
        print("JOGADA INVÁLIDA")
elif computador == 1:
    if jogador == 0:
        print("O COMPUTADOR VENCEU")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("VOCÊ VENCEU")
    elif jogador>= 3: 
        print("JOGADA INVÁLIDA")
elif computador == 2:
    if jogador == 0:
        print("O JOGADOR VENCEU")
    elif jogador == 1:
        print("O COMPUTADOR VENCEU")
    elif jogador == 2:
        print("EMPATE")
    elif jogador>= 3: 
        print("JOGADA INVÁLIDA")


