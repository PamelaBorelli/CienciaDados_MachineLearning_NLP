'''
Utilizando o código do exercício anterior, efetue alterações para permitir que o jogador reinicie uma nova partida e efetue a contagem de pontos do Computador e do Jogador.

'''

from random import randint

#entrada de dados



itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Escolha um opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
chave = True
tecla = ""
# pontoComputador = 0
# pontoJogador = 0



#processamento
while chave == True:
    # pontoComputador += 1
    # pontoJogador += 1


    jogador = int(input("Qual a sua opção: "))
    #dados de saída
    print("O computador escolheu   ==> {}".format(itens[computador]))
    print("O você escolheu         ==> {}".format(itens[jogador]))

    if computador == 0:
        if jogador == 0:
            print("EMPATE")
        elif jogador == 1:
            print("VOCÊ VENCEU")
        elif jogador == 2:
            print("O COMPUTADOR VENCEU")
        else: 
            print("JOGADA INVÁLIDA")
    elif computador == 1:
        if jogador == 0:
            print("O COMPUTADOR VENCEU")
        elif jogador == 1:
            print("EMPATE")
        elif jogador == 2:
            print("VOCÊ VENCEU")
        else: 
            print("JOGADA INVÁLIDA")
    elif computador == 2:
        if jogador == 0:
            print("VOCÊ VENCEU")
        elif jogador == 1:
            print("O COMPUTADOR VENCEU")
        elif jogador == 2:
            print("EMPATE")
        else: 
            print("JOGADA INVÁLIDA")

    # if computador == "O COMPUTADOR VENCEU":
    #     pontoComputador +=1
    #     print("ponto do computador: ", pontoComputador)
    # elif jogador == "VOCÊ VENCEU":
    #     pontoJogador +=1
    #     print("ponto do jogador: ", pontoJogador)
        
        
    tecla = str(input("Começar nova partida? <s/n> "))
    # while not (tecla =="S" or tecla =="s" or tecla =="N" or tecla =="n"):  
    if (tecla =="N" or tecla =="n"):
        chave = False


    
    