'''

"Sabe-se que o ano tem duração de 365 dias e os meses têm 30 ou 31 dias, sendo somente 
fevereiro com 28. Mas, de 4 em 4 anos, ocorre um ano bissexto, com 366 dias de duração (um dia 
a mais em fevereiro). Afinal, por que isso acontece?
O ano bissexto ocorre para ajustar o ano civil, que tem duração de 365 dias, com o ano solar, 
associado ao movimento de translação da Terra ao redor do Sol. 
O tempo que a Terra gasta para sair de uma posição de sua órbita e voltar novamente para este 
mesmo lugar é de 365,242189 dias, ou 365 dias, 5 horas, 48 minutos e 48 segundos, 
aproximadamente. Portanto, esta é a duração de um ano solar, diferente do ano civil.
Em 45 a.C., o astrônomo Sosígenes foi convocado por Júlio César para transformar o calendário 
romano em um calendário solar, alinhado pelas estações do ano, à semelhança do calendário 
egípcio já então em vigor. Ele estabeleceu o chamado ano comum, com 365 dias divididos em 12 
meses, alguns com 30 dias e outros com 31, de forma que em cada mês pudessem ser 
observadas as 4 fases da Lua. Além disso, acrescentou 1 dia de 3 em 3 anos, após 25 de 
fevereiro, criando assim o ano bissexto. O erro da inserção de anos bissextos de a cada três anos 
em vez de quatro foi detectado cerca de trinta anos mais tarde. 
Em 1582, o Papa Gregório reorganizou as datas e mudou o dia bissexto, que era 24 de fevereiro, para 
o dia 29 de fevereiro. O calendário gregoriano é usado até hoje na maior parte do planeta". 
[adaptado de https://www.ufmg.br/espacodoconhecimento/origem-anos-bissextos/]

Um ano é bissexto se: • Divisível por 4 - a divisão é exata com o resto igual a zero. • Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero; • Pode ser que seja divisível por 400, mas a divisão deve ser exata - o resto da divisão igual a zero.

Desenvolver um algoritmo e efetuar a implementação em Python para determinar se um ano é bissexto ou não.

'''

#entrada de dados
ano = int(input('Qual ano será analisado? : '))


#processamento e dados de saída
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))