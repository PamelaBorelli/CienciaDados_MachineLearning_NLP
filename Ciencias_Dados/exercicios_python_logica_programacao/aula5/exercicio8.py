'''
Desenvolver um algoritmo e efetuar a implementação em Python, para ler n nomes próprio e armazená-los em um vetor. O algoritmo também deve permitir a consulta de um nome específico, indicando se está ou cadastrado.

'''

#entrada de dados


quatNomes = int(input("Quantos nomes você quer incluir na lista? : "))

nomes  = []
nomeEscolhido = 0


#processamento e dados de saída
for i in range (0, quatNomes) :
    lista = str(input("Digite o {:.0f}º nome: ".format(i+1)))
    nomes.append(lista)
print("os nomes escolhidos foram: ", nomes)


#processamento e dados de saída
nomeEscolhido = str(input("Digite um  nome da lista: "))
if nomes.count(nomeEscolhido) > 0:
    print("o nome está na lista")
else:
    print("O nome não está na lista")



