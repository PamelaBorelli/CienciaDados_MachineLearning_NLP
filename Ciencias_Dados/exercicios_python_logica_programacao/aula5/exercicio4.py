'''
Desenvolver um algoritmo e efetuar a implementação em Python, para ler n valores inteiros, armazená-los 
em um vetor e efetuar a ordenação em ordem crescente. 

Utilizar o método sort() .

'''

import random

#entrada de dados
vetor = list(range(0,100))
random.shuffle(vetor)


#processamento
def selection_sort(v):
    i = 0
    while i < len(v) - 1 :
        menor = i
        j = i + 1
        while j < len(v):
            if v[j] < v[menor]:
                menor = j
            j += 1

        if menor != i:
            temp = v[i]
            v[i] = v[menor]
            v[menor] = temp
        i += 1

#dados de saída
selection_sort(vetor)
print(vetor)