'''
Utilizando o algoritmo do exercício [6], desenvolve um menu de opções para efetuar a conversão de 
temperatura entre TODAS as escalas, de acordo com a solicitação do usuário. 

Use a sua criatividade
'''


#entrada de dados
print("Qual escala de temperatura você quer converter")
print("Digite F para Fahreinheit, K para Kelvin, R para Réaumur ou RA para Rankine")
escolha = input()
print("Informe o valor da temperatura: ")
temperatura = float(input())


#processamento e dados de saída
if(escolha == "f" or escolha =="F"):
    print ('A temperatura de {:.2f}ºF corresponde a {:.2f}ºC'.format(temperatura,(5*(temperatura -32)/9)))
    
if(escolha == "k" or escolha == "K"):
    print ('A temperatura de {:.2f}ºK corresponde a {:.2f}ºC'.format(temperatura,(temperatura-273.15)))
   
if(escolha == "r" or escolha == "R"):
    print ('A temperatura de {:.2f}ºR corresponde a {:.2f}ºC'.format(temperatura,(temperatura/0.80000)))
    
if(escolha == "ra" or escolha == "RA"):
    print ('A temperatura de {:.2f}ºRA corresponde a {:.2f}ºC'.format(temperatura, ((5*temperatura)/9)-273.15))
    