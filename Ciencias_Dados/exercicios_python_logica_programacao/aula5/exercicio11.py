'''
Desenvolver um algoritmo e efetuar a implementação em Python, para ler n dados de alunos: RA e 4 Notas, armazena-las em uma matriz [n][6] e depois, calcular a média aritmética de cada aluno e armazená-la na última coluna [5] da matriz. Imprimir os dados formatados

'''

#entrada de dados
boletim = list()


#processamento e dados de saída
while True:
    nota1 = float(input("nota 1: "))
    nota2 = float(input("nota 2: "))
    nota3 = float(input("nota 3: "))
    nota4 = float(input("nota 4: "))
    media = (nota1 + nota2 + nota3 + nota4)/4
    boletim.append([nota1, nota2, nota3, nota4, media])
    continuar = str(input("incluir mais alunos? <s/n>"))
    if continuar in 'Nn':
        break


print(f'{"RA.":<4}{"NOTA1":<10}{"NOTA2":<10}{"NOTA3":<10}{"NOTA4":<10}{"MÉDIA":<10}')
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[1]:<10}{a[2]:<10}{a[3]:<10}{a[4]:<10.2f}')