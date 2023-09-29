'''
O Prof. Arcaxerxes Panturrilha deseja verificar se os seus alunos estão 
escrevendo as datas de forma correta. Assim, solicitou a você que 
desenvolva um algoritmo e efetue a implementação em Python para ler o 
dia, mês e ano verificando a consistência dos dados, por exemplo, se o 
mês está entre 1 e 12, se os dias estão entre 1 e 28, 30 ou 31 dias, de 
acordo com o mês correspondente e verifique se o ano é bissexto.

'''


#entrada de dados
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))




#processamento e dados de saída


# processamento dos dias do mês
if mes == 2 and ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0 and dia > 29: 
    print("O dia está entre o intervalo desse mês")
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11 ) and (dia <=30):    
    print("O dia está entre o intervalo desse mês")
elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and (dia <= 31):
    print("O dia está entre o intervalo desse mês")
else:
    print("O dia não está entre o intervalo desse mês")


# processamento dos meses do ano
if mes >=1 and mes <= 12:
    print("O mês está entre o intervalo")
else:
    print("Os dias não estão entre o intervalo desse mês")


# processamento se o ano é bissexto ou não
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))