import math
import statistics

# Imagine a seguinte situação: o dono de uma microempresa pretende saber, em média, quantos
# produtos são produzidos por cada funcionário em um dia. O chefe tem conhecimento que nem 
# todos conseguem fazer a mesma quantidade de peças, mas pede que os seus funcionários façam
# um registro da sua produção numa semana de trabalho. Ao fim desse período, chegou-se à
# seguinte tabela:

# 1) Variancia amostral:
funcA = [10, 9, 11, 12, 8]
funcB = [15, 12, 16, 10, 11]
funcC = [11, 10, 8, 11, 12]
funcD = [8, 12, 15, 9, 11]


def variancia(funcionario):
    # Calcula a média aritmética
    mA = sum(funcionario) / len(funcionario)

    va = 0
    for i in funcionario:
        va = va + pow(i - mA, 2)
    varAmostral = va / len(funcA)
    return round(varAmostral, 2)


print("\nVARIÂNCIA")
print("Funcionário A:", variancia(funcA))  # 2.0
print("Funcionário B:", variancia(funcB))  # 5.36
print("Funcionário C:", variancia(funcC))  # 1.84
print("Funcionário D:", variancia(funcD))  # 6.0


# 2) Desvio padrão amostral
def desvioPadrao(variancia):
    dp = math.sqrt(variancia)
    return round(dp, 2)


print("\nDESVIO PADRÃO")
print("Funcionário A:", desvioPadrao(variancia(funcA)))  # 1.41
print("Funcionário B:", desvioPadrao(variancia(funcB)))  # 2.32
print("Funcionário C:", desvioPadrao(variancia(funcC)))  # 1.36
print("Funcionário D:", desvioPadrao(variancia(funcD)))  # 2.45

# ------------------------------------------------------------------------------
# Érica adora postar as fotos do seu gato na ‘internet’. Cada
# uma das suas 6 últimas fotos receberam o seguinte número de
# "curtidas":
# 10,15,15,17,18,21

curtidas = [10, 15, 15, 17, 18, 21]


# 3) Desvio medio absoluto
def desvio_medio_absoluto(dados):
    media = statistics.mean(curtidas)
    desvioMedio = 0
    for dado in dados:
        dma = (dado - media)
        # Soma as distâncias com a média e obtem o módulo
        if dma < 0:
            desvioMedio += dma * (-1)
        else:
            desvioMedio += dma
    return desvioMedio


print("\nDESVIO MÉDIO ABSOLUTO")
print("Curtidas: ", round(desvio_medio_absoluto(curtidas) / len(curtidas), 2))  # 2,67


# 4) Desvio mediano absoluto
def dma(dados):
    # MAD = mediana (| xi - mediana(xi) |)
    mediana = statistics.median(dados)

    dma_curtidas = []
    desvioMediano = 0;
    for dado in dados:
        diff = (dado - mediana)
        if diff < 0:
            desvioMediano = (diff * (-1))
        else:
            desvioMediano = (dado - mediana)
        dma_curtidas.append(desvioMediano)
    return dma_curtidas


print("\nDESVIO MEDIANO ABSOLUTO")
print(dma(curtidas))  # [6.0, 1.0, 1.0, 1.0, 2.0, 5.0]
