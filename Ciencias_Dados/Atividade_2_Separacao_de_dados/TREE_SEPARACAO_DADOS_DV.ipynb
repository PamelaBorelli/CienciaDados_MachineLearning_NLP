# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 09:02:04 2023

@author: AM
"""

import os
import subprocess
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt #para gráficos
from sklearn import tree #Tem uma estrutura de árvore que será usada
from sklearn.tree import DecisionTreeClassifier #Classificador que gera uma árvore de regras


# #### Lendo Base de Dados - EFETUAR OS TESTES COM O BANCO DE DADOS REDUZIDO E O INTEGRAL
#db = pd.read_csv("D:\\PUC-CAMPINAS\\CURSO CPQD\\AULAS\\AULA016\\DATA SET EXEMPLO 001DD REDUZIDO.csv")
db = pd.read_csv("C:\\Users\\pamel\\OneDrive\\Área de Trabalho\\PucCampinas\\ciencias de dados\\aula22\\penguins.csv")

print("\n")
print(db)
print("************************************************************************")
# SELECIONAR OS CAMPOS
print("CAMPOS DO BANCO DE DADOS")  
campos=list(db)

for i in campos:
    print("\nCAMPO: ",i)
    print([i])
print("************************************************************************")  
input ("DIGITE ALGO:")
print("\n")


# SEPARANDO DADOS 
# [species[j],island[j],bill_length_mm[j],bill_depth_mm[j],
# flipper_length_mm[j],body_mass_g[j],sex[i]]
species = db['species'].copy() 
island = db['island'].copy() 
bill_length = db['bill_length_mm'].copy()
bill_depth = db['bill_depth_mm'].copy()
flipper_length = db['flipper_length_mm'].copy()
body_mass = db['body_mass_g'].copy()
sex = db['sex'].copy()



# CONTANDO O NÚMERO DE ESPECIES, ILHAS E GÊNERO
print("CONTANDO O NÚMERO DE ESPECIES, ILHAS E GÊNERO")
print('\n')
Qspecies=db.value_counts("species") 
print("CONTAR ESPECIES: \n",Qspecies)
print('\n')
Qisland=db.value_counts("island") 
print("CONTAR ILHAS: \n",Qisland)
print('\n')
Qsex=db.value_counts("sex") 
print("CONTAR GÊNERO: \n",Qsex)
print("************************************************************************")  
input ("DIGITE ALGO:")
print("\n")

# TRANSFORMANDO STRINGS DE ESPÉCIES PARA INT
print("TRANSFORMANDO STRINGS DE ESPÉCIES, ILHA, GÊNERO PARA INT")
db.loc[db.species == 'Adelie', 'species'] = 1
db.loc[db.species == 'Gentoo', 'species'] = 2
db.loc[db.species == 'Chinstrap', 'species'] = 3
#TRANSFORMANDO AS VARIAVEIS EM 'INT'
db['species'] = db['species'].astype('int')


# TRANSFORMANDO STRINGS DE ILHAS PARA INT
db.loc[db.island == 'Biscoe', 'island'] = 1
db.loc[db.island == 'Dream', 'island'] = 2
db.loc[db.island == 'Torgersen', 'island'] = 3
#TRANSFORMANDO AS VARIAVEIS EM 'INT'
db['island'] = db['island'].astype('int')


# TRANSFORMANDO STRINGS DE GÊNERO PARA INT
db.loc[db.sex == 'MALE', 'sex'] = 1
db.loc[db.sex == 'FEMALE', 'sex'] = 2

print(db)
print("************************************************************************")  
input ("DIGITE ALGO:")
print("\n")


# VERIFICANDO CAMPOS NULOS
print("VERIFICANDO CAMPOS NULOS")
print(db.isnull().sum(),
db[db.bill_length_mm.isnull()],
db[db.bill_depth_mm.isnull()],
db[db.flipper_length_mm.isnull()],
db[db.body_mass_g.isnull()],
db[db.sex.isnull()])
print("************************************************************************")  
input ("DIGITE ALGO:")
print("\n")



#VERIFICANDO PERCENTUAL DOS DADOS FALTANTES
print("VERIFICANDO PERCENTUAL DOS DADOS FALTANTES")
percentual_faltantes= (db.isnull().sum() / len(db['species']))* 100
print(percentual_faltantes)
print("************************************************************************")  
input ("DIGITE ALGO:")
print("\n")


# CORRIGINDO OS VALORES NULOS
print("CORRIGINDO OS VALORES NULOS")
db= db.drop(3, axis=0) 
db= db.drop(339, axis=0) 
db['sex']= db['sex'].fillna(2)
Q2sex=db.value_counts("sex")

print(db)
print("************************************************************************")  
input ("DIGITE ALGO:")
print("\n")

# VERIFICANDO SE OS VALORES NULOS FORAM ELIMINADOS
db.isnull().sum()
db[db.sex.isnull()]


print("DADOS ESTATÍSTICOS")
estatistica = db.describe()
print(estatistica)
print("\n")
print("CORRELAÇÃO")
correlacao = db.corr()
print(correlacao)
plt.rcParams["figure.figsize"] = (18,8)
ax = sns.heatmap(db.corr(), annot= True)
plt.show
print("************************************************************************")  
input ("DIGITE ALGO:")
print("\n")

sns.lmplot(y='flipper_length_mm', x = 'body_mass_g', data = db)
plt.show()
np.random.seed(1234)
df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
boxplot = df.boxplot(column=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']) 
plt.show()



#DETECTADO OUTLIERS E CORRIGINDO
print('DETECTADO OUTLIERS E CORRIGINDO')
print('\n')
#ENCONTRANDO O Q1 E Q3
print('ENCONTRANDO O Q1 E Q3')
massa= db.get(['body_mass_g'])
Q1 = np.percentile(massa, 25)
Q3 = np.percentile(massa, 75)
print('Q1: %.2f' %Q1)
print('Q3: %.2f' %Q3)

#CALCULANDO O INTERVALO INTERQUARTIL
print('\n')
print('CALCULANDO O INTERVALO INTERQUARTIL')
C= 1.5
IIQ = Q3 - Q1
LI = Q1 - C*IIQ
LS = Q3 + C*IIQ
print('IIQ:  %.2f' %IIQ)
print('LIMITES:')
print('INFERIOR:  %.2f' %LI)
print('SUPERIOR:  %.2f' %LS)

#ENCONTRANDO O MAIOR VALOR DA LISTA DE MASSA
max_value = max(db['body_mass_g'])
print('VALOR MÁXIMO NA LISTA:', max_value)
print("************************************************************************")  
input ("DIGITE ALGO PARA PLOT DE DADOS:")
print("\n")


# SEPARAR DADOS 
Species0=[]
Island0=[]
Blength0=[]
Bdepth0=[]
Flipper0=[]
Bmass0=[]
Sex0=[]

Species1=[]
Island1=[]
Blength1=[]
Bdepth1=[]
Flipper1=[]
Bmass1=[]
Sex1=[]


Species2=[]
Island2=[]
Blength2=[]
Bdepth2=[]
Flipper2=[]
Bmass2=[]
Sex2=[]



for i in range(len(island)):
    if species[i]=='Adelie':
        Species0.append(species[i])
        Island0.append(island[i])
        Blength0.append(bill_length[i])
        Bdepth0.append(bill_depth[i])
        Flipper0.append(flipper_length[i])
        Bmass0.append(body_mass[i])
        Sex0.append(sex[i])
    if species[i]=='Gentoo':
        Species1.append(species[i])
        Island1.append(island[i])
        Blength1.append(bill_length[i])
        Bdepth1.append(bill_depth[i])
        Flipper1.append(flipper_length[i])
        Bmass1.append(body_mass[i])
        Sex1.append(sex[i])
    if species[i]=='Chinstrap':  
        Species2.append(species[i])
        Island2.append(island[i])
        Blength2.append(bill_length[i])
        Bdepth2.append(bill_depth[i])
        Flipper2.append(flipper_length[i])
        Bmass2.append(body_mass[i])
        Sex2.append(sex[i])
       
        
plt.scatter(Species0,Island0,color="green") 
plt.scatter(Species1,Island1,color="blue")
plt.scatter(Species2,Island2,color="yellow")
plt.title("ADELIE(verde)  GENTOO(azul)  CHINSTRAP(amarelo) ")
plt.xlabel("ESPECIE")
plt.ylabel("ILHA")     
plt.show()
  
plt.scatter(Species0,Blength0,color="green") 
plt.scatter(Species1,Blength1,color="blue")
plt.scatter(Species2,Blength2,color="yellow")
plt.title("ADELIE(verde)  GENTOO(azul)  CHINSTRAP(amarelo) ")
plt.xlabel("ESPECIE")
plt.ylabel("COMPRIMENTO BICO")     
plt.show()     
        
plt.scatter(Species0,Bdepth0,color="green") 
plt.scatter(Species1,Bdepth1,color="blue")
plt.scatter(Species2,Bdepth2,color="yellow")
plt.title("ADELIE(verde)  GENTOO(azul)  CHINSTRAP(amarelo) ")
plt.xlabel("ESPECIE")
plt.ylabel("LARGURA BICO")     
plt.show()

plt.scatter(Species0,Flipper0,color="green") 
plt.scatter(Species1,Flipper1,color="blue")
plt.scatter(Species2,Flipper2,color="yellow")
plt.title("ADELIE(verde)  GENTOO(azul)  CHINSTRAP(amarelo) ")
plt.xlabel("ESPECIE")
plt.ylabel("NADADEIRA")     
plt.show()

plt.scatter(Species0,Bmass0,color="green") 
plt.scatter(Species1,Bmass1,color="blue")
plt.scatter(Species2,Bmass2,color="yellow")
plt.title("ADELIE(verde)  GENTOO(azul)  CHINSTRAP(amarelo) ")
plt.xlabel("ESPECIE")
plt.ylabel("MASSA")     
plt.show()

print("************************************************************************")  
input ("DIGITE ALGO PARA IMPRIMIR A ÁRVORE DE DECISÃO:")
print("\n")
# input ("DIGITE ALGO PLOT DADOS:")


# #### Criando classificador de árvore de decisão
# 
# A árvore de decisão procura cortes/intervalos 
# nos atributos de forma a dividir as classes o melhor possível; 
# gerando uma árvore de regras de decisão e nos informando 
# o quão separadas estão as classes em função dessa regra

# entropia é uma medida de caoticidade/'bagunça',
# utilizada para medir a mistura das classes dentro de uma regra,
# veremos ela logo
clf = DecisionTreeClassifier(criterion="entropy") 

# Os classificadores na biblioteca sklearn e scipy 
# esperam os dados (X) separados das metas/rótulos/classe (Y) 
# Vamos separar a coluna do rótulo

# drop (REMOVER) UMA COLUNA
dbAtributos = db.drop("island", axis=1, inplace=False)
print("\nDB ATRIBUTOS: \n",dbAtributos)


# SEPARA/COPIA O CAMPO "ESCOLAR"
#Em muitos casos o copy() não é necessário, mas é uma boa prática utilizá-lo
dbRotulos = db["island"].copy() 
print("\nDB RÓTULOS: \n",dbRotulos)


Arvore=clf.fit(dbAtributos, dbRotulos)
print("ARVORE: \n",Arvore)

# Imprimindo as regras geradas
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(30,30), dpi=300)
tree.plot_tree(clf, feature_names=dbAtributos.columns, class_names={0:"Ilha1", 1:"Ilha3", 2: "Ilha3" },filled=False)
plt.show()


# ### Interpretando a árvore de decisão
# 
# Lê-se um conjunto de regras pelo caminho entre raiz e as folhas da árvore. 
# cada nível inferior, novas regras são adicionadas, 
# filtrando amostras em grupos potencialmente menores, 
# mas mais homogêneos em relação à distribuição de classes, 
# essa homogeneidade pode ser medida de várias maneiras escolhemos a entropia.
# 
# Cada nó na árvore apresenta algumas informações:
# - Regra no formato atributo maior|menor|(igual) valor
# - Valor da medida de homogeineidade
# - Quantidade de amostras filtradas pelo conjunto de regras
# - Distribuição das classes na forma: [$qtdC_1, qtdC_2, ... qtdC_n$]
# - Classe majoritária filtrada pela regra (em caso de empate uma das duas é escolhida)
# - Cada regra possui um filho (outra regra ou separação) à esquerda (valores menores que a regra) e à direita

# ##### Entendendo entropia [1]
# 
# É uma medida de informação introduzida por Claude Shannon, 
# inclusive sendo chamada de entropia de Shannon. 
# Podemos interpretá-la como a quantidade de bits necessária para descrever um conjunto de dados, 
# dados homogêneos não carregam informação portanto consomem 0 bits, 
# já dois eventos com probabilidade igual de acontecer precisam de 1 bit. 
# e.g. Uma moeda que sempre dá cara não possui informação, 
# mas quando a moeda tem a chance de dar cara ou coroa temos uma situação mais complicada 
# com mais informação, notem que não podemos prever uma face ou outra; 
# agora imaginem um meio termo, a moeda tem uma chance muito grande de dar cara e uma menor de dar coroa, 
# ainda temos incerteza/informação, mas ainda conseguimos 'apostar' 
# com uma certa confiança que ela irá dar cara, portanto ela tem um pouco menos de informação/caoticidade 
# em relação à moeda equilibrada, a entropia será maior que 0, mas menor do que 1. 
# Quanto mais possibilidades diferentes (no nosso exemplo cara ou coroa), 
# maior o potencial de informação e maior é o valor máximo de entropia, 
# e.g. com 4 possíveis saídas a entropia máxima é 2 bits. 
# Abaixo veremos como a curva de entropia para dois valores: 


# ESTATISTICA
print("\n********************************")
print("ESTATÍSTICAS DA ARVORE:")
dbLabel=list(db.columns)
print("ROTULOS: ",dbLabel)
for pos,i in enumerate(dbLabel):
    print(pos," ",i)
# NÚMERO DE NÓS
n_nodes = clf.tree_.node_count
print("NÚMERO DE NÓS=",n_nodes)
children_left = clf.tree_.children_left
print("NÚMERO DE NÓS ESQUERDA=",children_left)
children_right = clf.tree_.children_right
print("NÚMERO DE NÓS DIREITA=",children_right)
feature = clf.tree_.feature
print("NÚMERO DE feature=",feature)
threshold = clf.tree_.threshold
print("NÚMERO DE threshold=",threshold)


# MONTANDO AS REGRAS DE PERCURSO
node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)

stack = [(0, 0)] 
# ENCONTRAR OS PONTOS TERMINAIS
while len(stack) > 0:
    # `pop` ensures each node is only visited once
    node_id, depth = stack.pop()
    node_depth[node_id] = depth

    # If the left and right child of a node is not the same we have a split
    # node
    is_split_node = children_left[node_id] != children_right[node_id]
    # If a split node, append left and right children and depth to `stack`
    # so we can loop through them
    if is_split_node:
        stack.append((children_left[node_id], depth + 1))
        stack.append((children_right[node_id], depth + 1))
    else:
        is_leaves[node_id] = True
        
print("A ÁRVORE TEM {n} NÓS - ESTRUTURA:\n".format(n=n_nodes))
    
for i in range(n_nodes):
    if is_leaves[i]:
        print(
            "{space}node={node} is a leaf node.".format(
                space=node_depth[i] * "\t", node=i
            )
        )
    else:
        print(
            "{space}node={node} is a split node: "
            "go to node {left} if X[:, {feature}] <= {threshold} "
            "else to node {right}.".format(
                space=node_depth[i] * "\t",
                node=i,
                left=children_left[i],
                feature=dbLabel[feature[i]],
                threshold=threshold[i],
                right=children_right[i],
            )
        )
        
        
# dbLabel LISTA DE LABEL
# feature[i]  regra label
# threshold[i]  valor menor <=
arvore=[[0]]
arvoreD=[["."]]

for i in range(n_nodes):
    if is_leaves[i]:
        print(
            "{space}node={node} is a leaf node.".format(
                space=node_depth[i] * "\t", node=i
            )
        )
    else:
        print(              
            "{space}node={node} is a split node: "
            "go to node {left} if X[:, {feature}] <= {threshold} "
            "else to node {right}.".format(
                space=node_depth[i] * "\t",
                node=i,
                left=children_left[i],
                feature=dbLabel[feature[i]],
                threshold=threshold[i],
                right=children_right[i],
               )            
             )
        # NÓ INICIAL
        inicio=i
        fims=children_left[i]
        fimn=children_right[i]
        auxarvore=[]
        auxarvoreD=[]
        for k in range(len(arvore)):
            if inicio in arvore[k]:
                auxs=arvore[k]+[fims]
                auxsD=arvoreD[k]+["E"]
                auxn=arvore[k]+[fimn]
                auxnD=arvoreD[k]+["D"]
                auxarvore.append(auxs)
                auxarvore.append(auxn)
                auxarvoreD.append(auxsD)
                auxarvoreD.append(auxnD)
            else:
                auxarvore.append(arvore[k])
                auxarvoreD.append(arvoreD[k])
        arvore=auxarvore  
        arvoreD=auxarvoreD
        print("\n\nARVORE:\n",arvore)

# DUPLICAR A ÚLTIMA DIREÇÃO        
i=0
TAMD=int(len(arvoreD))
while i< TAMD :
   arvoreD[i].append(arvoreD[i][len(arvoreD[i])-1])
   i=i+1
 
print("arvoreD:\n",arvoreD)
       
print("\n\n\n**********************************************")
# SELECIONAR DADOS DE UMA SEQUENCIA DE RAMOS
for pos,lin in enumerate(arvore):
    textoaux="" 
    auxDF=[]
    dbAux=db.copy()
    print("\nLIN: ",lin,"  ",arvoreD[pos])
    noD=-1
    for no in lin:
      noD=noD+1
      # PESQUISAR RAMOS ESQUERDA
      if arvoreD[pos][noD+1]=='E' :  
        if feature[no]>=0:  
          for j in range(0,len(dbAux)):
              if dbAux[dbLabel[feature[no]]][j]<=threshold[no] :
                  vl=[dbAux["IDADE"][j],dbAux["ALTURA"][j],dbAux["PESO"][j],dbAux["ECIVIL"][j],dbAux["ESCOLAR"][j]]
                  auxDF+=[vl]
          dbAux = pd.DataFrame(auxDF, columns=['IDADE','ALTURA','PESO','ECIVIL','ESCOLAR'])   
          textoaux=textoaux+dbLabel[feature[no]]+"<="+str(threshold[no])+" !! "
        auxDF=[]
      # PESQUISAR RAMOS DIREITA  
      if arvoreD[pos][noD+1]=='D':  
        if feature[no]>=0:  
          for j in range(0,len(dbAux)):
              if dbAux[dbLabel[feature[no]]][j]>threshold[no] :
                  vl=[dbAux["IDADE"][j],dbAux["ALTURA"][j],dbAux["PESO"][j],dbAux["ECIVIL"][j],dbAux["ESCOLAR"][j]]
                  auxDF+=[vl]
          dbAux = pd.DataFrame(auxDF, columns=['IDADE','ALTURA','PESO','ECIVIL','ESCOLAR'])   
          textoaux=textoaux+dbLabel[feature[no]]+">"+str(threshold[no])+" !! "
        auxDF=[]

        
    print("FIM DO RAMO: \n",textoaux,":\n",dbAux)

   
        
        
        






