# Atividade 4: Utilizando o exemplo da aula para calcular a assimetria
#              amostral de D1 e D2

from math import sqrt
from statistics import mean

d1 = [7, 10, 12, 15, 16, 18, 20]
d2 = [12, 15, 18, 23, 25, 26, 28]


def assimetriaAmostral(dados):
    media = mean(dados)

    lamb = 0
    va = 0
    for dado in dados:
        va += pow(dado - media, 2)  # calcula a somatoria da variâcia
        auxLamb = pow((dado - media), 3)  # calcula a somatoria da assimetria amostral

        # define todos os resultados como positivo
        if auxLamb < 0:
            lamb += auxLamb * (-1)
        else:
            lamb += auxLamb

    varAmostral = va / (len(dados) - 1)  # calcula a variancia
    dp = pow(sqrt(varAmostral), 3)  # calcula do desvio padrao da variancia elevado ao cubo
    return (lamb / dp) / (len(dados) - 1)  # retorna o resutado do calculo da assimetria amostral


print("Assimetria amostral de [D1]: ", assimetriaAmostral(d1))  # 1,21
print("Assimetria amostral de [D2]: ", assimetriaAmostral(d2))  # 1,13
