'''
Desenvolver um algoritmo e efetuar a implementação em Python para ler um número inteiro e efetuar a conversão para binário, armazenando os bits em um vetor

'''

#entrada de dados
num = int(input("Digite um número para converte-lo em binário: "))



#processamento e dados de saída
if num == 0:
    print("Numero inválido")
    
else:
    binario = ''
    while num > 1:
        resto = num % 2
        num = int(num/2)
        binario += str(resto)
    binario += '1'
    print(f"O valor de {num} convertido em binário é {binario[-1::-1]}")
    







