'''

Desenvolver um algoritmo e efetuar a implementação em Python para ler 
3 número e verificar se então em ordem crescente

'''

#entrada de dados
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o erceiro número: "))


#processamento e dados de saída
if (n1 > n2 or n1 > n2 or n2 > n3):
    print("Os números não estão em ordem crescente")
else:
    print("Os números estão em ordem crescente")