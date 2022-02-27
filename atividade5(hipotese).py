# Queremos verificar se duas máquinas produzem peças com a 
# mesma homogeneidade quanto a resistência à tensão. Para 
# isso, sorteamos dias amostras de 6 peças de cada máquina, 
# e obtivemos as seguintes resistências:
# Máquina A	145	127	136	142	141	137
# Máquina B	143	128	132	138	142	132

# FONTE: https://www.kaggle.com/educfrio/teste-de-hipotese

# Z = (x1-x1-var0) / sqrt((s²/n1)+(s²/n2))

# monta o teste de hipotese
# H0:
# Ha:
# retornar os três testes de hipotese ">, <, !="


from math import sqrt
from statistics import mean, stdev

# sqrt(3.214,0625) => 56,69270235224283
# z =-1,411183630269889

monitorA = [3412,3246,3183,3014,3531,3534,2738,3071,3546,3488,3395,3414,3429,3254,3683,2907,3410,2999,2908,3510,3092,3408,3216,3351,3127,3348,3275,2440,3245,3243,2888,3223,3267,2969]
monitorB = [2360,3011,3090,3203,2658,3072,3297,3618,3225,2755,2754,3242,2999,2715,2788,2994,2634,2504,3232,3507,3392,3167,3505,3111,3520,3188,3322,2471,3158,3288,3383,3029]
print("medias: ",mean(monitorA), mean(monitorB))

def testeHipotese(amostra1, amostra2, variancia1, variancia2, alpha):
  media1 = mean(amostra1)
  media2 = mean(amostra2)

  raiz = sqrt((pow(variancia1, 2)/n1)+(pow(variancia2, 2)/n2))
  variacaoMedia = media1 - media2
  zTeste = variacaoMedia/raiz
  print("zTeste: ",zTeste)

testeHipotese(monitorA, monitorB, 250, 300, 5)


media1 = 2290
media2 = 2370
variancia1 = 750
variancia2 = 800
n1 = 200
n2 = 200

raiz = sqrt((pow(variancia1, 2)/n1)+(pow(variancia2, 2)/n2))
variacaoMedia = media1 - media2
zTeste = (media1-media2)/raiz
print(zTeste) # -1.03