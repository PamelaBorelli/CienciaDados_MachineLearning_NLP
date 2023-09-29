'''
Jokenpô, também conhecido como “Pedra, Papel ou Tesoura”, é um jogo recreativo que permite a seleção de algum dos participantes. Utilizando os símbolos indicados:

• Pedra - indicada por um punho fechado - ganha da tesoura quebrando-a. 
• Tesoura - indicada por dois dedos separados e esticados - ganha do papel cortando-o. 
• Papel - indicado por uma mão aberta - ganha da pedra embrulhando-a.

Desenvolver um algoritmo e efetue a implementação em Python para um usuário jogar Jokenpô com o 
computador.

'''

from random import randint
import random

#entrada de dados
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
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
    
elif computador == 1:
    if jogador == 0:
        print("O COMPUTADOR VENCEU")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("VOCÊ VENCEU")
    
elif computador == 2:
    if jogador == 0:
        print("O JOGADOR VENCEU")
    elif jogador == 1:
        print("O COMPUTADOR VENCEU")
    elif jogador == 2:
        print("EMPATE")
    


