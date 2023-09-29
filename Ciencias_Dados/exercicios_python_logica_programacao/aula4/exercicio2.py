'''
Desenvolva um algoritmo e efetue a implementação em Python para ler n valores e imprimir o valor médio.

'''


#entrada de dados
cont = int(input("Digite a quantidade de notas para fazer a média: "))
notasMedia = 0  



#processamento
    
for i in range(0,cont):
    notas = (float(input("Digite a nota ")))
    notasMedia += notas
    
media = notasMedia/notas


#dados de saída
print("As notas são: ", notasMedia)
print("A media das notas é: ", media)




