'''
 Desenvolver um algoritmo e efetuar a implementação em Python, para ler dois números e informar se o 
primeiro é divisível pelo segundo. (NESTE CASO O RESTO DA DIVISÃO DEVE SER ZERO)

'''

#entrada de dados
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))


#processamento e dados de saída
if(num1 % num2 == 0):
    print("os números são divisíveis")
else:
    print("os números não são divisíveis")