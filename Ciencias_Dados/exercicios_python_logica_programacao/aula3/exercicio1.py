'''
Desenvolver um algoritmo e implementar em Python, para efetuar a leitura 
de uma senha numérica, efetuar a sua validação (senha pré-cadastrada) 
e escrever uma das seguintes mensagens: • “ACESSO PERMITIDO” caso a senha seja válida. • “ACESSO NEGADO” caso a senha seja inválida
'''
#entrada de dados
senhaLogin = "123"
senha = input("Digite a senha: ")

#processamento e saída
if(senha == senhaLogin):
    print("ACESSO PERMITIDO")
else:
    print('ACESSO NEGADO')
    