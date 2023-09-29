'''
Desenvolver um algoritmo e efetuar a implementação em Python, para ler as notas de n alunos, armazená-las em uma 
matriz e depois, calcular a média aritmética de cada aluno e armazená-la em outros vetor. 

O indexador de linha da matriz é o RA do aluno, e o aluno realiza 4 provas por semestre.


'''
#entrada de dados
boletim = list()

#processamento
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

#dados de saída
print(f'{"RA.":<4}{"NOTA1":<10}{"NOTA2":<10}{"NOTA3":<10}{"NOTA4":<10}{"MÉDIA":<10}')
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[1]:<10}{a[2]:<10}{a[3]:<10}{a[4]:<10.2f}')

while True:
    opc = int(input("Digite o RA do aluno para ver sua média ou digite 999 para FINALIZAR: "))
    if opc == 999:
        print("FINALIZAR")
        break
    if opc <= len(boletim) - 1:
        print(f" A media do aluno com RA{boletim[opc]} é {boletim[opc][4]}")
