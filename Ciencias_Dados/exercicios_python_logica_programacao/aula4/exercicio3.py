'''
Utilizando o código do exercício anterior, desenvolva um algoritmo e efetue a implementação em Python para ler n valores e imprimir o valor médio, o maior e o menor valor.

'''


#entrada de dados
cont = int(input("Digite a quantidade de notas para fazer a média: "))
soma = 0  
quant = 0


#processamento
for i in range(0,cont):
    notas = (float(input("Digite a {:.0f}º nota: ".format(i+1))))

    soma += notas
    quant +=1

    if quant == 1:
        maiorNota = menorNota = notas
    else: 
        if notas < menorNota:
            menorNota = notas 
        if notas > maiorNota:
            maiorNota = notas


media = soma/notas


#dados de saída
print("A soma das notas é: ", soma)
print("A a maior  nota é: ", maiorNota)
print("A a menor  nota é: ", menorNota)
print(F"A media das notas é: {media:6.2f}")



