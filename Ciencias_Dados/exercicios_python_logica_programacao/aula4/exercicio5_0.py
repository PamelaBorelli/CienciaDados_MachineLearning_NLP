'''
Desenvolva um algoritmo e efetue a implementação em Python para imprimir a tabuada de um número n:

'''

#entrada de dados
n = int(input(" digite um número: "))


#processamento e dados de saída
for i in range(1, 11):
    print( "{} x {} = {}".format(n, i, n*i))


