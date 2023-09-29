'''
Desenvolver um algoritmo e efetuar a implementação em Python, para ler o número n de linhas e imprimir uma pirâmide de 6*9

*
***
*****
*******
*********
***********


'''

#entrada de dados
n = 6



#processamento e dados de saída
for i in range (n):
    for j in range(n-i-1):
        print(" ", end = "")
    for j in range(i+1):
        print("#", end = " ")
    print()
