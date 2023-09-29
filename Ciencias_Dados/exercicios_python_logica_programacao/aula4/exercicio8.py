'''
Utilizando o código do exercício anterior, efetue alterações no algoritmo 
para apontar o número de tentativas até o acerto.

'''

import random


#entrada de dados


computador = random.randint(0,100)
numeroJogador = -1
tentativa = 0



#processamento e dados de saída
while(numeroJogador != computador):
    try:
        numeroJogador = int(input("digite o seu número: "))
        tentativa +=1

        if numeroJogador< computador:
            print("o seu nº é menor")
            
            
        elif numeroJogador> computador:
            print("o seu nº é maior")
            
        elif numeroJogador == computador:
            print("Acertou com {} tentativas. ".format(tentativa))
    except:
        print('Digite somente valores númericos')

    