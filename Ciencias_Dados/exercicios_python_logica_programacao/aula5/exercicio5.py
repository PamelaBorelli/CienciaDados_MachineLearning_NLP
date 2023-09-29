'''
Desenvolver um algoritmo e efetuar a implementação em Python, para ler n valores inteiros, armazená-los em um vetor e efetuar a ordenação em ordem crescente. NÃO utilizar o método sort(), desenvolver um algoritmo 
para comparar todos os valores efetuando a troca de posição dos valores 

'''

import random
#entrada de dados
vetor = list(range(0,10))


#processamento 3 dados de saída
random.shuffle(vetor)
print("Lista sorteda sem ordenar ===>", vetor)

lista = vetor
lista.sort()
print("Lista sorteda ordenada    ===>",lista)
