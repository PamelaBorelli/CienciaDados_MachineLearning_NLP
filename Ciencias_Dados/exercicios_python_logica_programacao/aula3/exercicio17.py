''' 
O Departamento de Trânsito de Rapidópolis está realizando uma campanha para orientar os proprietários de veículos quanto à data de pagamento do IPVA. Você foi contratado para desenvolver um algoritmo e efetuar a
implementação em Python, para ler o último dígito da placa do veículo, o mês corrente e escrever o mês de pagamento do imposto, mas se o mês corrente for superior ao mês de pagamento, deve-se emitir uma
mensagem informando que o pagamento mensagem informando que o pagamento está em atraso.

PLACA MÊS PAGAMENTO IPVA 

Final 1 – mês (1) – Janeiro
Final 2 – mês (2) – Fevereiro
Final 3 – mês (3) – Março
Final 4 – mês (4) – Abril
Final 5 – mês (5) – Maio
Final 6 – mês (6) – Junho
Final 7 – mês (7) – Julho
Final 8 – mês (8) – Agosto
Final 9 – mês (9) – Setembro
Final 0 – mês (10) – Outubro

'''

#entrada de dados
placa = []
for i in range(4):
    placa.append  (str(input(f'Digite os 4 últimos valores da placa: ')))

mesAtual= int(input("Qual o mês atual: "))

mesPlacaPagamento = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 10
}


#processamento

ultimoDigito = placa[-1]

if ultimoDigito not in mesPlacaPagamento:
    print('Placa inválida!')
    
mesPagamento = mesPlacaPagamento[ultimoDigito]


#dados de saída
if mesAtual > mesPagamento:
    print(f'Pagamento em atraso! O mês de pagamento do IPVA é {mesPagamento}.')
else:
    print(f'O mês de pagamento do IPVA é {mesPagamento}.')
