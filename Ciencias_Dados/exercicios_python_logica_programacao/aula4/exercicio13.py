'''
Desenvolva um algoritmo e efetue a implementação em Python imprimir os dados da lista indicada a seguir, apontando a sua posição sequencial:

'''


#entrada de dados
lista=["GUARANI", "SÃO PAULO", "PALMEIRAS", "CRUZEIRO", "SANTOS", "FERROVIÁRIA", "JUVENTUS", "GOIÁS", "ÍBIS", "SINOP"]

#processamento e dados de saída
for i,j in enumerate (lista):
    print(f"na posição {i} está o time {lista[i]}")