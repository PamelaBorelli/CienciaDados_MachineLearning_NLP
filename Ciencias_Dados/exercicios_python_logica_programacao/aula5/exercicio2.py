'''
Desenvolver um algoritmo e efetuar a implementação em Python, para ler n valores inteiros, armazená-los em um vetor e imprimir os dados na sequência inversa, do último valor para o primeiro

'''


#entrada de dados
lista = []
maior = 0
menor = 0
lista1 =[]



#processamento e dados de saída
for cont in range (0,5):
    lista.append(int(input(f"Digite o {cont+1}º número: ")))
    lista1 = lista[::-1]


    
print(f"Números digitados: {lista}")
print(f"Números digitados ao contratio: ", lista1)

