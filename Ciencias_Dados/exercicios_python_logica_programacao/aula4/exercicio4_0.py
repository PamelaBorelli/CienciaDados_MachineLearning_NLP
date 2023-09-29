'''
Desenvolva um algoritmo e efetue a implementação em Python para calcular a fatorial 
de um número n, onde a fatorial é definida por:

n! = n*(n-1)*(n-2) * ... *1

'''

from math import factorial


#entrada de dados
n = int(input("digite um numero: "))


#processamento
f = factorial(n)

#dados de saída
print("o Fatorial de {} é {}".format(n,f))