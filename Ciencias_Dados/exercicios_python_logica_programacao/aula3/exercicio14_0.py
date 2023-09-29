'''
O Prof. Arcaxerxes Panturrilha deseja verificar se os seus alunos estão 
escrevendo as datas de forma correta. Assim, solicitou a você que 
desenvolva um algoritmo e efetue a implementação em Python para ler o 
dia, mês e ano verificando a consistência dos dados, por exemplo, se o 
mês está entre 1 e 12, se os dias estão entre 1 e 28, 30 ou 31 dias, de 
acordo com o mês correspondente e verifique se o ano é bissexto.

'''

# Essa foi a primeira tentativa mas não funciona, o próximo algoritmo funciona


dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))

anoBissexto = ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0

print(f'A data informado é: {dia}/{mes}/{ano}')

if (mes == 1) and (dia >= 1 and dia <= 31):
    print("O dia não está entre o intervalo desse mês")
if mes == 5 and (dia >= 1 and dia <= 31):
    print("O dia não está entre o intervalo desse mês")
if mes == 7 and (dia >= 1 and dia <= 31):
    print("O dia não está entre o intervalo desse mês")
if mes == 8 and (dia >= 1 and dia <= 31):
    print("O dia não está entre o intervalo desse mês")
if mes == 10 and (dia >= 1 and dia <= 31):
    print("O dia não está entre o intervalo desse mês")
if mes == 12 and (dia >= 1 and dia <= 31):
    print("O dia não está entre o intervalo desse mês")
else:
    print("O dia está entre o intervalo desse mês")


if mes == 4 and dia < 30:
    print("O dia não está entre o intervalo desse mês")
if mes == 6 and dia < 30:
    print("O dia não está entre o intervalo desse mês")
if mes == 9 and dia < 30:
    print("O dia não está entre o intervalo desse mês")
if mes == 11 and dia < 30:
    print("O dia não está entre o intervalo desse mês")
else:
    print("O dia está entre o intervalo desse mês")


if mes == 2 and dia < 29: 
    if ano != anoBissexto:
       print("O dia não está entre o intervalo desse mês1")
else:
    print("O dia está entre o intervalo desse mês1")



if mes >=1 and mes <= 12:
    print("O mês está entre o intervalo")
else:
    print("Os dias não estão entre o intervalo desse mês")

if ano == anoBissexto:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))




