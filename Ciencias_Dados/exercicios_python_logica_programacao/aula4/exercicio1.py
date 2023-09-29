'''
Desenvolva um algoritmo e efetue a implementação em Python para ler dois valores e imprimir os valores inteiros no intervalo.

'''

#entrada de dados
inicial = 0
parada = 0
inicial= int(input("Digite um número para começar a leitura: "))
parada = int(input("Digite um número para terminar a leitura: "))


#processamento e dados de saída
for cont in range (inicial,parada+1):
    if inicial < parada:
        print("Valores do intervalo = ", cont)


