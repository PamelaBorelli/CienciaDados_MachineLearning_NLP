'''
Desenvolver um algoritmo e efetuar a implementação em Python para calcular o valor da função f(x). Atenção: 

NÃO É PERMITIDO EFETUAR A DIVISÃO POR ZERO.

'''

#entrada de dados
x= float(input('digite um valor para x: '))
input("--------------------------------------------------------------------------------------------")


#processamento e dados de saída
input('\n')
while x == 0:
    print('NÃO É PERMITIDO EFETUAR A DIVISÃO POR ZERO.')
    print('Digite outro número')
    break
else: 
    funcao = (4* x**2 - 3*x+9)/x
    print('O Resultado da função é: ', funcao)




