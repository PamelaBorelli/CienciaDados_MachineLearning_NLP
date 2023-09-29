'''
Desenvolver um algoritmo e efetuar a implementação em Python, para ler n valores inteiros, armazená-los em um vetor e calcular o maior e o menor valor, e calcular a média aritmética.

'''
#entrada de dados



lista = []
maior = 0
menor = 0


#processamento e dados de saída
for cont in range (0,5):
    lista.append(int(input(f"Digite o {cont+1}º número: ")))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]


print(f"Números digitados: {lista}")


print("O maior valor digitado: {}".format(int(maior)))
print("O maior valor digitado: {}".format(int(menor)))

print("\n")
print(f"O maior valor digitado: {maior}", end="")
print(f"O menor valor digitado: {menor}", end="")