'''
Em Rapidópolis, a cada 2 anos, ocorrem eleições para o Congresso ou Câmara do Comuns. A participação no processo eleitoral, ou seja, os votantes, devem seguir as seguintes regras:

• não eleitor (abaixo de 16 anos);
• eleitor obrigatório (entre a faixa de 18 e menor de 
65 anos);
• eleitor facultativo (de 16 até 18 anos e maior de 65 
anos, inclusive).

desenvolver um algoritmo para efetuar a leitura da idade de um eleitor e efetuar a classificação quando a possibilidade de votação nas eleições em Rapidópolis. 
Efetue a implementação em Python tratando exceções 
de dados durante a execução do programa.

'''

#entrada de dados
idade = int(input("Digite sua idade: "))



#processamento e dados de saída
if idade < 16:
    print("Não eleitor (abaixo de 16 anos)")

if idade >=16 and idade <18:
    print("eleitor facultativo (de 16 até 18 anos )")

if idade >= 18 and idade < 65:
    print("leitor obrigatório (entre a faixa de 18 e menor de 65 anos")

if idade >= 65:
    print(" eleitor facultativo (maior de 65 anos).")