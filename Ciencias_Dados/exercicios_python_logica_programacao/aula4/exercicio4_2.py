'''
Desenvolva um algoritmo e efetue a implementação em Python para calcular a fatorial 
de um número n, onde a fatorial é definida por:

n! = n*(n-1)*(n-2) * ... *1

'''

#entrada de dados
n = int(input("digite um número: "))
cont = 1

#processamento
print('Calculando {}! = '.format(n), end = "")
for n in range(n,0,-1):
    print('{}'.format(n), end = "")
    print(' x ' if n > 1 else ' = ', end = "")
    cont *= n

#dados de saída
print("{}".format(cont))
