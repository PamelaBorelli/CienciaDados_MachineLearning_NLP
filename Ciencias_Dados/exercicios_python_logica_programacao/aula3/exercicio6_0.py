'''
    No Brasil a unidade para aferição de temperatura é o grau Celsius oC, mas pode-se utilizar outras escalas, como o Fahrenheit (utilizada em países de língua inglesa), Kelvin, Rankine (em algumas áreas da Engenharia nos Estados Unidos) e Réaumur e muitas outras que estão em desuso (como Rφmer, Newton e Delisle).

    Desenvolver o algoritmo e implementar em Python, para efetuar a conversão de graus Fahrenheit, Kelvin, Rankine e Réaumur em graus Celsius. 
    
'''

# Fiz essa atividade errada, fica como extra.

#entrada de dados
from fractions import Fraction
fracao = Fraction(9,5)
celcius = float(input('Informe a temperatuca ºC: '))
fahrenheit  = float ((9*celcius/5)+32)
kelvin = float (celcius+273.25)
reaumur = float ((4*(fahrenheit-32))/9)
rankine = float (fracao*(celcius+ 273.15))


#processamento e dados de saída
print ('A temperatura de {:.2f}ºC corresponde a {:.2f}ºF'.format(celcius,fahrenheit))
print ('A temperatura de {:.2f}ºC corresponde a {:.2f}ºK'.format(celcius,kelvin))
print ('A temperatura de {:.2f}ºC corresponde a {:.2f}ºR'.format(celcius,reaumur))
print ('A temperatura de {:.2f}ºC corresponde a {:.2f}ºRA'.format(celcius,rankine))