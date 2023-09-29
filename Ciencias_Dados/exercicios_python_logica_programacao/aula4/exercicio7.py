'''
 Em Rapidópolis, as Escolas de Educação Infantil utilizam ferramentas computacionais como instrumento de aprendizagem e ensino. Você foi contratado para desenvolver um algoritmo e implementar em Python, 
para implementar o jogo: “Adivinhe o número”. O computador deve gerar um número inteiro entre 0 e 100 e o usuário deverá adivinhá-lo. Para cada tentativa, informe ao usuário se o número informado é maior, menor ou igual ao gerado pelo computador.

import random

# GERAS NÚMERO
numeroComputador=random.randint(0,100) 
ANDRÉ
MENDELECK numeroComputador=random.randint(0,100) 
print("\n**********************************") n**********************************")
print("JOGO: ADIVINHE O NÚMERO (0 a 100) ("JOGO: ADIVINHE O NÚMERO (0 a 100)\n")
numeroJogador numeroJogador=-1
while numeroJogador numeroJogador!=numeroComputador numeroComputador:
numeroJogador numeroJogador=int(input("DIGITE UM NÚMERO: ")) (input("DIGITE UM NÚMERO: "))
if(numeroJogador numeroJogador>numeroComputador numeroComputador):
print("O seu número é MAIOR que o do computador") ("O seu número é MAIOR que o do computador")
if(numeroJogador numeroJogador<numeroComputador numeroComputador):
print("O seu número é MENOR que o do computador") ("O seu número é MENOR que o do computador") 
if(numeroJogador numeroJogador==numeroComputador numeroComputador):
print("\nPARABÉNS nPARABÉNS, VOCÊ ACERTOU O NÚMERO")

'''

import random

computador = random.randint(0,100)
numeroJogador = -1

while(numeroJogador != computador):
    try:
        numeroJogador = int(input("digite o seu número: "))

        if numeroJogador< computador:
            print("o seu nº é menor")
        if numeroJogador> computador:
            print("o seu nº é maior")
        if numeroJogador == computador:
            print("PARABÈNS você acertou")
    except:
        print('Digite somente valores númericos')