'''
Os comerciantes do Mercado Municipal de Rapidópolis estabeleceram um percentual de margem mínima de lucro em função do valor do produto:

Valor DO Produto (VP) < R$ 25,00 Lucro de 100%
R$ 25,00 ≤ VP < R$ 100,00 Lucro de 70%
R$ 100,00 ≤ VP < R$ 500,00 Lucro de 60%
R$ 500,00 ≤ VP < R$ 1000,00 Lucro de 50% 
VP ≥ R$ 1000,00 Lucro de 40%

Desenvolver um algoritmo para efetuar a leitura do valor do produto e apontar o percentual mínimo de lucro.
Efetue a implementação em Python tratando exceções de dados durante a execução do programa.

'''

#entrada de dados
valorProduto= float(input("Digite o valor do produto: "))


#processamento e dados de saída
if valorProduto < 25:
    print("O percentual de lucro é 100%")

if valorProduto >= 25  and valorProduto < 100:
    print("O percentual de lucro é 75%")

if valorProduto >= 100 and valorProduto < 500:
    print("O percentual de lucro é 60%")

if valorProduto >=500 and valorProduto < 1000:
    print("O percentual de lucro é 50%")

if valorProduto >= 1000:
    print("O percentual de lucro é 45%")