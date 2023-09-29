'''
 A Universidade Hogwarts de Rapidópolis está contratando você para 
desenvolver um algoritmo e efetuar a implementação em Python para 
calcular a média dos seus alunos e verificar o nível de frequência. Os 
alunos realizam duas avaliações: Aval1 e Aval2 , com o mesmo peso. 
Calcular a média aritmética. Para aprovação os alunos precisam ter 
pelo menos 75% de presença nas atividades acadêmicas. Utilizar os 
dados da tabela a seguir para indicar o status acadêmico do aluno. 
Imprimir um boletim, contendo a nota, o status de frequência e o status 
acadêmico.

STATUS NOTA e FREQUÊNCIA                                STATUS ACADÊMICO 
Freqüência até 75%                                      Reprovado 
Freqüência entre 75% e 100% e Nota até 4.0              Reprovado 
Freqüência entre 75% e 100% e Nota de 4.0 até 6.0       Exame 
Freqüência entre 75% e 100% e Nota entre 6.0 e 10.0     Aprovado


'''

#tentei fazer usando uma condição extra com o número de frequencia sendo digitado com '%' mas estava dando conflito na resposta

nota1 = float(input("Digite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))

frequencia = str(input("Digite a porcentagem de frequencia do aluno: "))
media = float ((nota1 + nota2) /2)

print("Nota do aluno: ", media)
print("Frequencia do aluno: ", frequencia)

# Freqüência eaté 75%
if ((frequencia < "75" or frequencia < "75%")):
    print("Aluno reprovado")

# Freqüência entre 75% e 100% e Nota até 4.0 
if ((media < 4 ) or ((frequencia >= "75" or frequencia >= "75%") and (frequencia <= "100" or frequencia <= "100%"))):
    print("Aluno reprovado1")
    
# Freqüência entre 75% e 100% e Nota de 4.0 até 6.0 
if ((media >= 4 and media < 6) and (frequencia > "75" or frequencia > "75%" )):
    print("Aluno de exame")
    
# Freqüência entre 75% e 100% e Nota entre 6.0 e 10.0 
if ((media >=6  and media <= 10) and (frequencia >= "75" or frequencia >= "75%" )):
     print("Aluno aprovado")