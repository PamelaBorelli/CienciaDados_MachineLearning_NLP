'''
Desenvolver um algoritmo e efetuar a implementação em 
Python para converter metros por segundo em quilômetros 
por hora.
'''

#entrada de dados de m/s
metros = float(input('Digite a distância em metros (m): '))
segundos = float(input('Digite o tempo em segundo: '))
input("--------------------------------------------------------------------------------------------")

#processamento
medidaMS = metros/segundos
#dados de saída
print('A distência em m/s é: ',(medidaMS), 'm/s')


#entrada de dados km/h
km= metros/1000
hr = segundos/3600
#processamento
medidaKmH = km/hr
#dados de saída
print('A distência em km/h é: ',(medidaKmH), 'km/h')





