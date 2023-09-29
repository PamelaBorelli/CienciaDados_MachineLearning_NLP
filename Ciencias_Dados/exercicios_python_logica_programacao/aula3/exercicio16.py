'''
Utilizando o algoritmo desenvolvido no exercício anterior, efetue a leitura de números float entre 0 e 999, com duas casas decimais e escreve o valor por extenso.

'''
#entrada de dados
input("Digite a logo abaixo um número, começando pela centena, depois dezena, depois unidade." + "\n"+ "Se a opção for vazia digite '0' (zero)")
input("--------------------------------------------------------------------------------------------")

c = str(input('Digite a centena: '))
d = str(input('Digite a dezena: '))
u = str(input('Digite a unidade: '))

c = c + d + u # convertendo os números em uma lista

cFloat = float(c)
print("O número digitado foi: ", cFloat) #convertendo a lista em número float


#processamento e dados de saída

#condição para centenas
if c == '9':
    print('novecentos e ', end=' ')

elif c == '8':
    print('oitocentos e ', end=' ')

elif c == '7':
    print('setecentos e ', end=' ')

elif c == '6':
    print('seiscentos e ', end=' ')

elif c == '5':
    print('quinhentos e ', end=' ')

elif c == '4':
    print('quatrocentos e ', end=' ')

elif c == '3':
    print('trezentos e ', end=' ')
elif c == '2':
    print('duzentos e ', end=' ')

elif c == '1':
    if d==0 and u==0:
        print('cem', end=' ')
    elif c==1 and d!=0 and u !=0:
        print('cento e', end=' ')


#condição para centenas
if d == '9':
    print('noventa e', end=' ')

elif d == '8':
    print('oitenta e', end=' ')

elif d == '7':
    print('setenta e', end=' ')

elif d == '6':
    print('sessenta e', end=' ')

elif d == '5':
    print('cinquenta e', end=' ')

elif d == '4':
    print('quarenta e', end=' ')

elif d == '3':
    print('trinta e', end=' ')

elif d == '2':
    print('vinte e', end=' ')

elif d == '1':
    if u=='0':
        print('dez', end=' ')
    elif u=='1':
        print('onze', end=' ')

    if u=='2':
        print('doze', end=' ')

    if u=='3':
        print('treze', end=' ')

    if u=='4':
        print('quatorze', end=' ')

    if u=='5':
        print('quinze', end=' ')

    if u=='6':
        print('dezesseis', end=' ')

    if u=='7':
        print('dezessete', end=' ')

    if u=='8':
        print('dezoito', end=' ')

    if u=='9':
        print('dezenove', end=' ')


#condição para unidades
if d !='1':
    if u == '9':
        print('nove ponto zero', end=' ')

    elif u == '8':
        print('oito ponto zero', end=' ')

    elif u == '7':
        print('sete ponto zero', end=' ')

    elif u == '6':
        print('seis ponto zero', end=' ')

    elif u == '5':
        print('cinco ponto zero', end=' ')
    
    elif u == '4':
        print('quatro ponto zero', end=' ')

    elif u == '3':

        print('três ponto zero', end=' ')

    elif u == '2':
        print('dois ponto zero', end=' ')

    elif u == '1':
        print('um ponto zero', end=' ') 