'''
A ERA : Empresa Rapidopolense de Alimentação está desenvolvendo uma pesquisa abordando a redução no consumo de calorias em função da idade. Após inúmeras avaliações identificou-se o seguinte perfil:

• Crianças abaixo de 5 anos, devem consumir, em média, no máximo 2500 Calorias/Diárias
• Jovens entre 6 e 15 anos, devem consumir, em média, no máximo 2100 Calorias/Diárias
• Jovens Adultos entre 16 e 30 anos, devem consumir, em média, no máximo 2000 
Calorias/Diárias
• Adultos entre 31 e 60 anos, devem consumir, em média, no máximo 1800 Calorias/Diárias
• Adultos com mais de 60 anos, devem consumir, em média, no máximo 1600 Calorias/Diárias

Desenvolver um algoritmo para efetuar a leitura da idade de uma pessoa e efetuar a classificação quando ao consumo máximo de calorias escrevendo o valor correspondente. Efetue a implementação em Python tratando exceções de dados durante a execução do programa.

'''


#processamento
idade = int(input("Digite sua idade: "))




#dados de saída e entrada de dados
if idade < 6:
    print("Você pode consumir, em média, no máximo 2500 Calorias/Diárias)")

if idade >=6 and idade <=15:
    print("Você pode consumir, em média, no máximo 2100 Calorias/Diárias")

if idade >= 16 and idade <= 30:
    print("Você pode em média, no máximo 2000 Calorias/Diárias")

if idade >= 31 and idade <= 60:
    print("Você pode em média, no máximo 1800 Calorias/Diárias")

if idade >= 61:
    print("Você pode em média, no máximo 1600 Calorias/Diárias")