'''
Desenvolva um algoritmo e efetue a implementação em Python para calcular a fatorial 
de um número n, onde a fatorial é definida por:

n! = n*(n-1)*(n-2) * ... *1

'''


#entrada de dados
n = int(input("digite um número: "))
c = n
f = 1 


#processamento
print('Calculando {}! = '.format(n), end = "")
while c > 0:
    print('{}'.format(c), end = "")
    print(' x ' if c > 1 else ' = ', end = "")
    f *= c
    c-=1


#dados de saída
print("{}".format(f))