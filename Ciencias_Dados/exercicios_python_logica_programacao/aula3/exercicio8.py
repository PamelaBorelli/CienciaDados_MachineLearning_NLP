'''
Em Rapidópolis, a prefeitura proporciona desconto do IPTU em função da idade do imóvel: 

IDADE < 5 anos 0%
IDADE >=5 e IDADE < 20 15% 
IDADE >=20 e IDADE < 40 25%
IDADE >= 40 30%

Desenvolver um algoritmo e realizar a implementação em Python, para efetuar a leitura do ano
de construção do imóvel, do ano atual, calcular a idade do imóvel e calcular o percentual
de desconto do IPTU.

'''


#entrada de dados
anoConstrucao = int(input("Digite o ano de construção do imóvel: "))
anoAtual = int(input("Digite o ano atual: "))
idadeImovel = int(anoAtual - anoConstrucao)

#processamento e dados de saída
print('Idade do imóvel: ',idadeImovel,' anos')
if(idadeImovel < 5):
    print('O seu imóvel tem direito a 0 de desconto')
elif(idadeImovel >=5 and idadeImovel< 20):
    print('O seu imóvel tem direito a 15 de desconto')
elif(idadeImovel >=20 and idadeImovel< 40):
    print('O seu imóvel tem direito a 25 de desconto')
elif(idadeImovel >=40):
    print('O seu imóvel tem direito a 30 de desconto')