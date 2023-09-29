'''
Utilizando o código do exercício anterior, efetue alterações para que o usuário indique o número que será utilizado para indicar a divisibilidade.

'''
#entrada de dados
inicial = 0
parada = 0
divisibilidade = 0 


#processamento e dados de saída
inicial= int(input("Digite um número para começar a leitura: "))
parada = int(input("Digite um número para terminar a leitura: "))
divisibilidade = int(input("Digite um número para indicar a divisibilidade: "))

for cont in range (inicial,parada+1):
    if inicial < parada and cont %divisibilidade ==0:
        print("Valores do intervalo divisíveis por 3 são = ", cont)