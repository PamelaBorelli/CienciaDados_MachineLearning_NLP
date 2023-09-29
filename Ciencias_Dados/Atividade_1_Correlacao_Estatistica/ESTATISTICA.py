# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 22:21:15 2023

@author: dAVId
"""


import matplotlib.pyplot as plt
import numpy as np
import random

import pandas as pd
from pandas import read_csv
from pandas import set_option
import time as tm
# FFT
from numpy.fft import fft, ifft

dados=[]


# *********************
# * LEITURA DOS DADOS *
# *********************
import csv
path = "D:\\Google\\Curso Mescla\\Projeto\\sinaisvitais003 100dias DV2 RA2379.txt"
with open(path,'r',newline='') as ARQUIVO:
 d = csv.reader(ARQUIVO)
 dd=list(d)
 for i in range(0,len(dd)):
  p=dd[i][0]  
  palavras=p.split("\t")
  dados.append({"HORA":palavras[0],"BATIMENTO":palavras[1],"PRESSAO":palavras[2],"TEMPERATURA":palavras[3]})
  
  
# **********************************
# * SEPARAR OS CAMPOS PARA ANALISE *
# **********************************
hora=[]
batimento=[]
pressao=[]
temperatura=[]
for i in range(0,len(dados)):
    hora.append(dados[i]["HORA"])
    batimento.append(float(dados[i]["BATIMENTO"]))
    pressao.append(float(dados[i]["PRESSAO"]))
    temperatura.append(float(dados[i]["TEMPERATURA"]))



# ************************************
# * CALCUALR A MEDIA DE DOIS VALORES *
# ************************************
def media(v1,v2):
  return (v1+v2)/2

#****************************************
# PRE-PROCESSAMENTO
# 0 <= Batimento <= 200
# 0 <= pressao <= 25
# 0 <= temperatura <= 50 
#****************************************
for i in range(1,len(dados)-1):
    if (batimento[i]<0) or (batimento[i]>100):
        batimento[i]=media(batimento[i-1],batimento[i+1])
    if (pressao[i]<0) or (pressao[i]>25):
        pressao[i]=media(pressao[i-1],pressao[i+1])
    if (temperatura[i]<0) or (temperatura[i]>50):
        temperatura[i]=media(temperatura[i-1],temperatura[i+1])

        
#****************************************
# ESTATISTICA BASICA
#****************************************

somaBatimento=0
mediaBatimento=0
maxBatimento=-100
minBatimento=100000

somaPressao=0
mediaPressao=0
maxPressao=-100
minPressao=100000

somaTemperatura=0
mediaTemperatura=0
maxTemperatura=-100
minTemperatura=100000

histoBatimento=[]
histoPressao=[]
histoTemperatura=[]
for i in range(0,100):
    histoBatimento.append(int(0))
    histoPressao.append(int(0))
    histoTemperatura.append(int(0))

for i in range(0,len(dados)):
  somaBatimento=somaBatimento+float(batimento[i])
  somaPressao=somaPressao+float(pressao[i])
  somaTemperatura=somaTemperatura+float(temperatura[i])
  if (float(batimento[i])>maxBatimento):
      maxBatimento=float(batimento[i])
  if (float(pressao[i])>maxPressao):
      maxPressao=float(pressao[i])
  if (float(temperatura[i])>maxTemperatura):
      maxTemperatura=float(temperatura[i])
      
  if (float(batimento[i])<minBatimento):
      minBatimento=float(batimento[i])
  if (float(pressao[i])<minPressao):
      minPressao=float(pressao[i])
  if (float(temperatura[i])<minTemperatura):
      minTemperatura=float(temperatura[i])
      
  histoBatimento[int(batimento[i])]=histoBatimento[int(batimento[i])]+1
  histoPressao[int(pressao[i])]=histoPressao[int(pressao[i])]+1
  histoTemperatura[int(temperatura[i])]=histoTemperatura[int(temperatura[i])]+1
      
mediaBatimento=somaBatimento/len(dados)
mediaPressao=somaPressao/len(dados)
mediaTemperatura=somaTemperatura/len(dados)

print("**********************************")
print("TAMANHO DA AMOSTRA = ",len(dados))
print(" ")
print("BATIMENTO MÉDIO =",mediaBatimento)
print("BATIMENTO MÁXIMO =",maxBatimento)
print("BATIMENTO MÍNIMO =",minBatimento)
print(" ")
print("PRESSAO MÉDIA =",mediaPressao)
print("PRESSAO MÁXIMA =",maxPressao)
print("PRESSAO MÍNIMA =",minPressao)
print(" ")
print("TEMPERATURA MÉDIA =",mediaTemperatura)
print("TEMPERATURA MÁXIMA =",maxTemperatura)
print("TEMPERATURA MÍNIMA =",minTemperatura)


#HISTOGRAMA BATIMENTO CARDIACO
plt.hist(batimento)
plt.xlabel("BATIMENTO")
plt.ylabel("FREQUENCIA")
plt.show()

plt.plot(histoBatimento[int(minBatimento)-1:int(maxBatimento)+2],color='darkblue')
xb=np.arange(int(minBatimento)-1,int(maxBatimento)+2)
xb1=np.arange(0,len(xb))
plt.xticks(xb1,xb,rotation='vertical')
plt.xlabel("BATIMENTO")
plt.ylabel("FREQUENCIA")
plt.show()

#HISTOGRAMA PRESSAO ARTERIAL
plt.hist(pressao)
plt.xlabel("PRESSAO")
plt.ylabel("FREQUENCIA")
plt.show()

plt.plot(histoPressao[int(minPressao)-1:int(maxPressao)+2],color='darkgreen')
xp=np.arange(int(minPressao)-1,int(maxPressao)+2)
xp1=np.arange(0,len(xp))
plt.xticks(xp1,xp,rotation='vertical')
plt.xlabel("PRESSAO")
plt.ylabel("FREQUENCIA")
plt.show()

#HISTOGRAMA TEMPERATURA
plt.hist(temperatura)
plt.xlabel("TEMPERATURA")
plt.ylabel("FREQUENCIA")
plt.show()

tp=histoTemperatura[int(minTemperatura)-1:int(maxTemperatura)+2]
plt.plot(tp,color='yellow')
xt=np.arange(int(minTemperatura)-1,int(maxTemperatura)+2)
xt1=np.arange(0,len(xt))
plt.xticks(xt1,xt,rotation='vertical')
plt.xlabel("TEMPERATURA")
plt.ylabel("FREQUENCIA")
plt.show()

############################################################################
# NOVO TRATAMENTO
###########################################################################
# MEDIANA
auxDFMediana=[]
auxDFMediana+=[(batimento[j],pressao[j],temperatura[j]) for j in range(0,len(dados))]
DFdadosMediana=pd.DataFrame(auxDFMediana, columns=["BATIMENTO","PRESSÃO","TEMPERATURA"])
MedianaBatimento=[]
MedianaTemperatura=[]
MedianaPressao=[]

# MEDIA
auxDFMedia=[]
auxDFMedia+=[(batimento[j],pressao[j],temperatura[j]) for j in range(0,len(dados))]
DFdadosMedia=pd.DataFrame(auxDFMedia, columns=["BATIMENTO","PRESSÃO","TEMPERATURA"])
MediaBatimento=[]
MediaTemperatura=[]
MediaPressao=[]

# MODA
auxDFModa=[]
auxDFModa+=[(batimento[j],pressao[j],temperatura[j]) for j in range(0,len(dados))]
DFdadosModa=pd.DataFrame(auxDFModa, columns=["BATIMENTO","PRESSÃO","TEMPERATURA"])
ModaBatimento=[]
ModaTemperatura=[]
ModaPressao=[]

# DESVIO PADRAO
auxDFDesvioPadrao=[]
auxDFDesvioPadrao+=[(batimento[j],pressao[j],temperatura[j]) for j in range(0,len(dados))]
DFdadosDesvioPadrao=pd.DataFrame(auxDFDesvioPadrao, columns=["BATIMENTO","PRESSÃO","TEMPERATURA"])
DesPadTemperatura=[]
DesPadBatimento=[]
DesPadPressao=[]


# SEPARANDO PACOTES
totalHoras=24

pacotes=int(len(dados)/totalHoras)
print("\nNÚMERO TOTAL DE PACOTES PARA ANÁLISE:  ",pacotes)
for i in range(pacotes-1):
    Pbatimento=batimento[i*totalHoras:(i+1)*totalHoras]
    Ppressao=pressao[i*totalHoras:(i+1)*totalHoras]
    Ptemperatura=temperatura[i*totalHoras:(i+1)*totalHoras]
    
#   PRINT MEDIANA
print("\nMediana 100 DIAS")
print("*******************************************************")
medianaT = DFdadosMediana.median()
print(medianaT)
print("*******************************************************")
t=input("Aperte Qualquer tecla para continuar:")
for i in range(pacotes-1):    
    PauxDFMediana=[]
    PauxDFMediana+=[(Pbatimento[j],Ppressao[j],Ptemperatura[j]) for j in range(0,totalHoras)]
    PDFdadosMediana=pd.DataFrame(PauxDFMediana, columns=["BATIMENTO","PRESSÃO","TEMPERATURA"])
    
    print("*******************************************************")
    print("ANALISANDO MEDIANA DO PACOTE:  ",i)

    mediana = PDFdadosMediana.median()
    if mediana["BATIMENTO"] > medianaT["BATIMENTO"]:
        print(f"ACIMA DA BATIMENTO NORMAL! {medianaT['BATIMENTO']}")
    if mediana["TEMPERATURA"] > medianaT["TEMPERATURA"]:
            print(f"ACIMA DA TEMPERATURA NORMAL! {medianaT['TEMPERATURA']}")
    if mediana["PRESSÃO"] > medianaT["PRESSÃO"]:
                print(f"ACIMA DA PRESSÃO NORMAL! {medianaT['PRESSÃO']}")
    print(mediana)

    MedianaBatimento.append(mediana["BATIMENTO"])
    MedianaTemperatura.append(mediana["TEMPERATURA"])
    MedianaPressao.append(mediana["PRESSÃO"])
t=input("Aperte Qualquer tecla para continuar:")

# MEDIA
print("\nMEDIA 100 DIAS")
print("*******************************************************")
mediaT = DFdadosMedia.mean()
print(mediaT)
print("*******************************************************")
t=input("Aperte Qualquer tecla para continuar:")
for i in range(pacotes-1):    
    PauxDFMedia=[]
    PauxDFMedia+=[(Pbatimento[j],Ppressao[j],Ptemperatura[j]) for j in range(0,totalHoras)]
    PDFdadosMedia=pd.DataFrame(PauxDFMedia, columns=["BATIMENTO","PRESSÃO","TEMPERATURA"])
    
    print("*******************************************************")
    print("ANALISANDO MEDIA DO PACOTE:  ",i)

    media = PDFdadosMediana.mean()
    if media["BATIMENTO"] > mediaT["BATIMENTO"]:
        print(f"ACIMA DA BATIMENTO NORMAL! {mediaT['BATIMENTO']}")
    if media["TEMPERATURA"] > mediaT["TEMPERATURA"]:
            print(f"ACIMA DA TEMPERATURA NORMAL! {mediaT['TEMPERATURA']}")
    if media["PRESSÃO"] > mediaT["PRESSÃO"]:
                print(f"ACIMA DA PRESSÃO NORMAL! {mediaT['PRESSÃO']}")
    print(media)

    MediaBatimento.append(media["BATIMENTO"])
    MediaTemperatura.append(media["TEMPERATURA"])
    MediaPressao.append(media["PRESSÃO"])
t=input("Aperte Qualquer tecla para continuar:")


# MODA
print("\nMODA 100 DIAS")
print("*******************************************************")
for coluna in DFdadosModa.columns:
    modaT = DFdadosModa[coluna].mode()[0]
    print(f"Moda da coluna {coluna}: {modaT}")
    if coluna == "BATIMENTO":
        ModaBatimento.append(modaT)
    elif coluna == "TEMPERATURA":
        ModaTemperatura.append(modaT)
    elif coluna == "PRESSÃO":
        ModaPressao.append(modaT)
print("*******************************************************")
t=input("Aperte Qualquer tecla para continuar:")    
for i in range(pacotes-1):    
    PauxDFModa=[]
    PauxDFModa+=[(Pbatimento[j],Ppressao[j],Ptemperatura[j]) for j in range(0,totalHoras)]
    PDFdadosModa=pd.DataFrame(PauxDFModa, columns=["BATIMENTO","PRESSÃO","TEMPERATURA"])
    
    print("*******************************************************")
    print("ANALISANDO MODA DO PACOTE:  ",i)

    for coluna in PDFdadosModa.columns:
        moda = PDFdadosModa[coluna].mode()[0]
        print(f"Moda da coluna {coluna}: {moda}")
        if coluna == "BATIMENTO":
            ModaBatimento.append(moda)
        elif coluna == "TEMPERATURA":
            ModaTemperatura.append(moda)
        elif coluna == "PRESSÃO":
            ModaPressao.append(moda)
t=input("Aperte Qualquer tecla para continuar:")

# 
print("\nDESVIO PADRÃO 100 DIAS")
print("*******************************************************")
desvio_padraoT = DFdadosDesvioPadrao.std()
print(desvio_padraoT)
print("*******************************************************")
t=input("Digite Qualquer tecla para continuar:") 
for i in range(pacotes-1):    
    PauxDFDesvioPadrao=[]
    PauxDFDesvioPadrao+=[(Pbatimento[j],Ppressao[j],Ptemperatura[j]) for j in range(0,totalHoras)]
    PDFdadosDesvioPadrao=pd.DataFrame(PauxDFDesvioPadrao, columns=["BATIMENTO","PRESSÃO","TEMPERATURA"])
    
    print("*******************************************************")
    print("ANALISANDO DESVIO PADRÃO DO PACOTE:  ",i)

    desvio_padrao = DFdadosDesvioPadrao.std()
    if desvio_padrao["BATIMENTO"] > desvio_padraoT["BATIMENTO"]:
        print(f"ACIMA DA BATIMENTO NORMAL! {desvio_padraoT['BATIMENTO']}")
    if desvio_padrao["TEMPERATURA"] > desvio_padraoT["TEMPERATURA"]:
            print(f"ACIMA DA TEMPERATURA NORMAL! {desvio_padraoT['TEMPERATURA']}")
    if desvio_padrao["PRESSÃO"] > desvio_padraoT["PRESSÃO"]:
                print(f"ACIMA DA PRESSÃO NORMAL! {desvio_padraoT['PRESSÃO']}")
    print(desvio_padrao)

    DesPadBatimento.append(desvio_padrao["BATIMENTO"])
    DesPadTemperatura.append(desvio_padrao["TEMPERATURA"])
    DesPadPressao.append(desvio_padrao["PRESSÃO"])
    
    
   
# plt.plot(batimento,color='darkblue')
# x=np.arange(len(hora))
# plt.xticks(x,hora,rotation='vertical')
# plt.xlabel("HORA")
# plt.ylabel("BATIMENTO")
# plt.show()


# fig, ax = plt.subplots(figsize=(15,5))
# ax.plot(hora,batimento, 'o', label='BATIMENTO',color='darkblue')
# ax.plot(hora,pressao, 'd', label='PRESSAO',color='darkgreen')
# ax.plot(hora,temperatura, 'v', label='TEMPERATURA',color='yellow')
# #ax.set_xticks(np.arange(0,len(hora)),['0',"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"])
# ax.set_xlabel('HORA')
# ax.legend();


# fig1, ax1 = plt.subplots(figsize=(15,5))
# ax1.plot(hora,pressao, 'd', label='PRESSAO',color='darkblue')
# ax1.set_xlabel('HORA')
# ax1.set_ylabel('PRESSAO')
# ax1.legend();


# fig2,ax2 = plt.subplots(figsize=(15,5))
# n, bins, patches = ax2.hist(batimento,color='darkblue') 
# ax2.set_xlabel('BATIMENTO')
# ax2.set_ylabel('OCORRENCIAS')
# ax2.legend();






