'''
O IMC (Índice de Massa Corporal) foi 
criado pelo matemático Lambert 
Quételet para permitir a padronização 
para a análise do peso de uma pessoa. 
O cálculo é muito simples:

imc = peso/ (altura **2)

Onde o PESO é em Kg e a ALTURA em metros. O valor do IMC 
pode ser classificado de acordo com os dados listados na 
tabela ao lado.

Menor que 18,5 = Abaixo do peso

Entre 18,5 e 24,9 = Peso normal

Entre 25 e 29,9 = Sobrepeso (acima do peso desejado)

Igual ou acima de 30 = Obesidade

fonte: Biblioteca Virtual em Saúde - Ministério da saúde


*Professor, não encontrei a tabela no exercício, então estou usando as informações do site
do Ministério da saúde. Abaixo tem o link de acesso

https://bvsms.saude.gov.br/obesidade-18/#:~:text=Classifica%C3%A7%C3%A3o%20do%20IMC%3A%20Menor%20que%2018%2C5%20%E2%80%93%20Abaixo,desejado%29%20Igual%20ou%20acima%20de%2030%20%E2%80%93%20Obesidade

Desenvolver um algoritmo e efetuar a implementação em 
Python, para calcular o IMC. 
'''

#entrada de dados
#dados de saída
#processamento



#dados de entrada
peso = float(input('Informe o peso (kg): '))
altura = float(input('Informe a altura (m): '))

imc = peso/ (altura **2)
imc = round(imc,2)

#dados de saída
print('\n','Seu imc é: ', (imc))   

#processamento
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25.1 <= imc < 30:
    print('Você está com sobrepeso.')
elif imc >= 30:
    print('Você está com obesidade.')