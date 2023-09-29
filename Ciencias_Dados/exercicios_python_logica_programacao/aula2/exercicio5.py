'''
Os alunos dos Curso de Sistemas de Informação e Computação da PUCCampinas estão desenvolvendo um novo 
sistema de GPS cartesiano. Uma base inercial (Geo Base) referenciada, é posicionada no Campus, sendo o ponto 
de origem para a obtenção de coordenadas [X,Y] da posição.

'''

import math


#entrada de dados
A = (-1,2)
B = (3,-1)

#processamento
print(f"As coordenadas x: {A}, coordenadas y: {B}".format(A,B))
dist = math.sqrt( ((B[0] - A[0])**2) + ((B[1] - A[1]**2) ))

#dados de saída
print(f'A distancia entre os pontos {A} e {B} é igual a: {round(dist,2)}')