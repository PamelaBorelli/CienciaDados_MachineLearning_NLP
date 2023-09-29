'''
Desenvolva um algoritmo e efetue a implementação em Python para ler dois valores (inicial e final) de um intervalo e indique os números que são divisíveis por 3.

'''

#entrada de dados
inicial = 0
parada = 0

#processamento e dados de saída
inicial= int(input("Digite um número para começar a leitura: "))
parada = int(input("Digite um número para terminar a leitura: "))

for cont in range (inicial,parada+1):
    if inicial < parada and cont %3 ==0:
        print("Valores do intervalo divisíveis por 3 são = ", cont)