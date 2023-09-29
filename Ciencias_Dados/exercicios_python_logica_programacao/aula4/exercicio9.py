'''
Utilizando o código do exercício anterior, efetue alterações no algoritmo para proporcionar a possibilidade do jogador desistir da partida.

'''

import random



#entrada de dados
continuar= "s"
numeroJogador = -1
computador = random.randint(0,100)
tentativa = 0


#processamento e dados de saída
while continuar =="s":
    numeroJogador = int(input("digite o seu número: "))
    controle = "s"
    tentativa += 1

    if numeroJogador != computador:
        if numeroJogador< computador:
            print("o seu nº é menor")
        if numeroJogador> computador:
            print("o seu nº é maior")
        if numeroJogador == computador:
            print("Acertou com {} tentativas. ".format(tentativa))
        
    if numeroJogador == computador:
        print("Acertou com {} tentativas. ".format(tentativa))
    if numeroJogador != computador:
        continuar = str(input(('Deseja continuar <s/n>: ')))

else:
    print("TCHAU!!")
        


