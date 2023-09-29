'''
O Topógrafo Dr. Dystancyus Perímetrus coletou as coordenadas de uma gleba rural, na região de Rapidópolis, cujo mapa é apresentado na figura abaixo. Desenvolva um algoritmo e efetue a implementação em Python para ler as coordenadas de cada ponto, armazenar em uma matriz e efetuar o cálculo do perímetro da fazenda.

'''


#entrada de dados
array = [(200,200), 
         (800,200), 
         (800,300), 
         (1600,300), 
         (1600,200), 
         (2100,500), 
         (2100,1100), 
         (1700,1400), 
         (300,1400), 
         (500,800), 
         (500,500), 
         (200,500)
]


#processamento
def Gauss_area(array):
    a = 0
    ox,oy = array[0]
    for x,y in array[1:]:
        a += (x*oy-y*ox)
        ox,oy = x,y
    print('A área do polígono é igual a: {:.2f}'.format(abs(a/2)))


#dados de saída
Gauss_area(array)
