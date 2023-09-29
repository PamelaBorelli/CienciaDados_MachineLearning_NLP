'''

No IRC – Instituto Rapodopolense de Computação o cálculo da nota final de uma disciplina é efetuado com a ponderação das notas bimestrais parciais. No semestre o aluno realiza duas provas (Prova1 e Prova2). 

A média final é calculada ponderando os valores com os pesos Peso1 para a prova 1 e Peso2 para a prova 2:

No boletim do aluno deverá aparecer o valor das notas, os pesos e as seguintes mensagens: 

•Se média < 5, escrever “REPROVADO”
•Se média >= 5, escrever “APROVADO”
•Se média >= 8 e média < 9 , escrever “PARABÉNS O DESEMPENHO FOI MUITO BOM”
•Se média >= 9, escrever “PARABÉNS, VOCÊ FOI APROVADO COM LOUVOR”

'''

#entrada de dados


prova1 = float(input('Digite a 1º nota: '))
prova2 = float(input('Digite a 2º nota: '))
peso1 = float(input('Digite o 1º peso: '))
peso2 = float(input('Digite o 2º peso: '))

#processamento
media = ((prova1 * peso1) + (prova2 * peso2)) / (peso1 + peso2)

#dados de saída
if(media < 5):
    print('REPROVADO')

elif(media >=5 ):
    print('APROVADO')

elif(media >= 8 and media < 9):
    print('PARABÉNS O DESEMPENHO FOI MUITO BOM')

elif(media >= 9):
    print('PARABÉNS, VOCÊ FOI APROVADO COM LOUVOR')
