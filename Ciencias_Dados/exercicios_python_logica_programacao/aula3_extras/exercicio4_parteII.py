'''
A VITOR : Vinículas Internacionais, Terrotoriais e Orgânicas de Rapidópolis, após extensos estudos enológicos, classificou os vinhos Rapidopolen em categorias

•Extra Secos: até 2 gramas de açúcar por litro. 
•Secos: de 2,1 a 4 gramas de açúcar por litro. 
•Meio secos: de 4,1 a 25 gramas de açúcar por litro. 
•Suaves: de 25,1 a 50 gramas de açúcar por litro. 
•Doces: de 50,1 a 180 gramas de açúcar por litro. 
•Extra Doces ou Fortificados: mais que 180 gramas de açúcar por litro.

Desenvolver um algoritmo para efetuar a leitura da quantidade de açúcar no vinho e efetuar a classificação quando à categoria. 
Efetue a implementação em Python tratando exceções de dados durante a execução do programa

'''



#processamento
acucar = float(input("Digite a quantidade de açúcar no vinho para obter sua classificação: : "))


#dados de saída e entrada de dados
if acucar <= 2:
    print("Esse vinho é classificado como: Extra Seco ")

if acucar >=2.1 and acucar <=4 :
    print("Esse vinho é classificado como: Seco")

if acucar >= 4.1 and acucar <= 25:
    print("Esse vinho é classificado como: Meio seco")

if acucar >= 25.1 and acucar <= 50:
    print("Esse vinho é classificado como: Suave")

if acucar >= 50.1 and acucar <= 180:
    print("Esse vinho é classificado como: Doce")

if acucar >= 180.1:
    print("Esse vinho é classificado como: Extra Doces ou Fortificados")