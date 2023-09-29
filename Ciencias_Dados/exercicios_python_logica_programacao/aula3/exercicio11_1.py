
nota1 = float(input("Digite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))

frequencia = int(input("Digite a porcentagem de frequencia do aluno: "))
media = float ((nota1 + nota2) /2)

print("media do aluno: ", media)
print("Frequencia do aluno: ", frequencia)

# Freqüência eaté 75%
if frequencia < 75 :
    print("Aluno reprovado")
elif frequencia >= 75 :
    if media < 4.0 : # Freqüência entre 75% e 100% e Nota até 4.0 
        print("Aluno reprovado")
    if media >= 4.0 and media < 6.0: # Freqüência entre 75% e 100% e Nota de 4.0 até 6.0 
       print("Aluno de exame")
    if media >= 6.0  and media <= 10.0: # Freqüência entre 75% e 100% e Nota entre 6.0 e 10.0
        print("Aluno aprovado")

