'''
Na Bohrgogna de Rapidópolis, o processo de vinificação dos gran cru, utiliza-se tanques de concreto com monitoramento de temperatura. O concreto, diferentemente das barricas de carvalho, é um elemento neutro, incorporando pouquíssimas características ao vinho. A fermentação é iniciada a zero graus Celsius, sofre uma redução e no final do processo atinge temperaturas positivas. O monitoramento da temperatura é fundamental, pois, o tanque pode sofrer rachaduras. A curva padrão de temperatura durante a fermentação é função do nível médio de açúcar no mosto (resultado do esmagamento e/ou prensagem dos bagos de uva). Neste ano de 2055, a safra de uvas Syrah foi muito boa, sendo chamada de a safra das safras, pois, o clima e o terroir contribuíram fortemente para a maturação dos cachos. O enólogo chefe, Dr. Tempranillo Camenére Nebbiolo, após receber os dados do laboratório de análises químicas, determinou a curva de temperatura de fermentação:


   T(0) = 0.011*dia**3-0.3*dia**2+0.04*dia


Onde d indica o dia do mês (0 a 30) e T(d) a temperatura. O processo de fermentação não pode 
ultrapassar 30 dias. 

Desenvolva um algoritmo e efetue a implementação em Python, para calcular o dia com a menor 
temperatura prevista para o processo de fermentação de acordo com a equação definida pelo enólogo.

'''


#entrada de dados
menorTemperatura = 0.011*0**3-0.3*0**2+0.04*0
menorDia = 0


#processamento
for dia in range (1,30+1):
    temperatura = 0.011*dia**3-0.3*dia**2+0.04*dia
    print("DIA  = ", dia, "TEMPERATURA = ",temperatura,"ºC")
    print(f"DIA ={dia:5d} TEMPERATURA = {temperatura:6.2f}ºC")
    print("\n")

    if temperatura < menorTemperatura:
        menorTemperatura = temperatura
        menorDia = dia


#dados de saída
print('Menor Temperatura = ', menorTemperatura)
print("No dia ", menorDia, " ocorreu a menor temperatura= ", menorTemperatura)