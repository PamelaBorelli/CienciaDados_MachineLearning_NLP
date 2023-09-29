'''
Utilizando o algoritmo do exercício [6], desenvolve um menu de opções para efetuar a conversão de 
temperatura entre TODAS as escalas, de acordo com a solicitação do usuário. 

Use a sua criatividade
'''


#entrada de dados


print("Qual escala de temperatura você quer converter")
print("Digite F para Fahreinheit, K para Kelvin, R para Réaumur ou RA para Rankine")
escolha = input()
print("Informe o valor da temperaturana escala que você quer converter: ")
temperatura = float(input())
print('Em qual escala está a temperatura que você quer converter')
conversao = input()


#processamento e dados de saída

#conversões de Farenheit
if((escolha == "f" or escolha =="F") and (conversao == "k" or conversao =="K")):
    print ('A temperatura de {:.2f}ºF corresponde a {:.2f}ºK'.format(temperatura,(temperatura + 459.67)*(5/9)))

if((escolha == "f" or escolha =="F") and (conversao == "c" or conversao =="C")):
    print ('A temperatura de {:.2f}ºF corresponde a {:.2f}ºC'.format(temperatura, ((5*(temperatura -32)/9))))

if((escolha == "f" or escolha =="F") and (conversao == "r" or conversao =="R")):
    print ('A temperatura de {:.2f}ºF corresponde a {:.2f}ºR'.format(temperatura, (4*(temperatura-32)/9)))

if((escolha == "f" or escolha =="F") and (conversao == "ra" or conversao =="RA")):
    print ('A temperatura de {:.2f}ºF corresponde a {:.2f}ºRA'.format(temperatura,(temperatura + 459.67)))



#conversões de Kelvin
if((escolha == "k" or escolha =="K") and (conversao == "f" or conversao =="F")):
    print ('A temperatura de {:.2f}ºK corresponde a {:.2f}ºF'.format(temperatura,(1.8 * (temperatura-273.15)+32)))

if((escolha == "k" or escolha =="K") and (conversao == "c" or conversao =="C")):
    print ('A temperatura de {:.2f}ºK corresponde a {:.2f}ºC'.format(temperatura,(temperatura-273.15)))

if((escolha == "k" or escolha =="K") and (conversao == "r" or conversao =="R")):
    print ('A temperatura de {:.2f}ºK corresponde a {:.2f}ºR'.format(temperatura,((temperatura-273.15)*0.80000)))

if((escolha == "k" or escolha =="K") and (conversao == "ra" or conversao =="RA")):
    print ('A temperatura de {:.2f}ºK corresponde a {:.2f}ºRA'.format(temperatura,(temperatura* (9/5))))


#Escolha de escala Réaumur
if((escolha == "r" or escolha =="R") and (conversao == "f" or conversao =="F")):
    print ('A temperatura de {:.2f}ºK corresponde a {:.2f}ºF'.format(temperatura,((temperatura*2.2500) +32)))

if((escolha == "r" or escolha =="R") and (conversao == "c" or conversao =="C")):
    print ('A temperatura de {:.2f}ºK corresponde a {:.2f}ºC'.format(temperatura, ((temperatura)* (5/4))))

if((escolha == "r" or escolha =="R") and (conversao == "k" or conversao =="K")):
    print ('A temperatura de {:.2f}ºK corresponde a {:.2f}ºR'.format(temperatura,((temperatura / 0.80000)+273.15)))

if((escolha == "r" or escolha =="R") and (conversao == "ra" or conversao =="RA")):
    print ('A temperatura de {:.2f}ºK corresponde a {:.2f}ºRA'.format(temperatura,((temperatura * 2.2500)+ 491.67)))
   

#Escolha Rakime
if((escolha == "ra" or escolha =="RA") and (conversao == "f" or conversao =="F")):
    print ('A temperatura de {:.2f}ºK corresponde a {:.2f}ºF'.format(temperatura,((temperatura- 491.67) +32)))

if((escolha == "ra" or escolha =="RA") and (conversao == "c" or conversao =="C")):
    print ('A temperatura de {:.2f}ºK corresponde a {:.2f}ºC'.format(temperatura, ((temperatura - 491.67)/1.8000)))

if((escolha == "ra" or escolha =="RA") and (conversao == "k" or conversao =="K")):
    print ('A temperatura de {:.2f}ºK corresponde a {:.2f}ºR'.format(temperatura,(((temperatura -491.67)/1.8000)+273.15)))

if((escolha == "ra" or escolha =="RA") and (conversao == "r" or conversao =="R")):
    print ('A temperatura de {:.2f}ºK corresponde a {:.2f}ºRA'.format(temperatura,((temperatura -491.67)* 0.44444)))