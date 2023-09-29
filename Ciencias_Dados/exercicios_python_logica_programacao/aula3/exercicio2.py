'''
Desenvolver um algoritmo e efetuar a implementação em Python, para ler o comprimento dos 3 lados de um triângulo e indicar a sua classificação:

•Triângulo Equilátero: possui os 3 lados iguais. 
•Triângulo Isóscele: possui 2 lados iguais.
•Triângulo Escaleno: possui 3 lados diferentes
'''
#entrada de dados
lado1 = float(input('Primeiro lado: '))
lado2 = float(input('Segundo lado: '))
lado3 = float(input('Terceiro lado: '))

#processamento e dados de saída
if lado1 < lado2 + lado3 and lado2 < lado1 + lado2 + lado3 and lado3 < lado2 + lado1:
    print('Os segmentos acima formam um triângulo ==> ', end="")
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO')
    elif lado1 != lado2 != lado3 != lado1:
        print("ESCALENO")
    else:
        print('ISÓSCELES')

else:
    print('Não é possível formar um triângulo, tente de novo.')
    print('\n')