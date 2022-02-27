import math
import statistics
rows = [7, 6, 7, 6, 7, 4, 5, 7, 5, 8, 6, 5, 5, 7, 8, 4, 7, 7, 7, 6]
# Medidas de tendencia central
# - Média amostral
# - Mediana amostral 
# - Moda amostral
def media_amostral(dados):
  somatoriaDados=0
  for dado in dados:
    somatoriaDados += dado
  return somatoriaDados/len(dados)


def mediana_amostral(dados):
  dados.sort()
  # calculo da mediana amostral
  for i in range(len(dados)):
    if len(dados) % 2 == 0: # se n for positivo
      index = int((len(dados) / 2))
      med = dados[index] - 0.5
    else: # se n for negativo
      index = int((len(dados)+1) / 2)
      med = dados[index-1]
  return med

def moda_amostral(dados):
  dados.sort()
  amostra = []
  frequencia = []
  for dado in dados:
    if dado in amostra:
      pass
    else:
      amostra.append(dado)
      frequencia.append(dados.count(dado))

  # definindo a moda
  maior=0
  for i in range(len(frequencia)):
    if frequencia[i] > maior:
      maior = frequencia[i]
      moda = amostra[i]
  return moda


# Medidas de dispersão
# - Desvio Padrão 
# - Variancia
# - Desvio médio absoluto
def variancia_amostral(dados):
  # Calcula a média aritmética
  media = statistics.mean(dados)

  va = 0
  for dado in dados:
    va += pow((dado-media), 2)
  varAmostral = va / (len(dados)-1)
  return varAmostral

def desvio_padrao(variancia):
  dp = math.sqrt(variancia)
  return dp

def desvio_medio_absoluto(dados):
  media = statistics.mean(dados)
  desvioMedio = 0
  for dado in dados:
    dma = (dado - media)
    # Soma as distâncias com a média e obtem o módulo
    if dma < 0:
      desvioMedio += dma * (-1) # torna tudo positivo
    else:
      desvioMedio += dma
  return round(desvioMedio,2)

# Separatrizes
# - Quartil
# Fonte: https://edtisensei.zendesk.com/hc/pt-br/articles/360050448172-C%C3%A1lculo-dos-quartis
# 1. Separar os dois lados do array a partir da mediana
# 2. Colocalos en um novo array cada
# 3. tentar encontrar a mediana de cada um
def qualtil(dados):
  dados.sort()
  n = len(dados)
  q1=[]; q3=[]
  index = (n+1)/2
  for i in range(n):
    if i < (index-1):
      q1.append(dados[i])
    if i > (index-1):
      q3.append(dados[i])
  primQuantil = statistics.median(q1)
  segQuantil = statistics.median(dados)
  tercQuantil = statistics.median(q3)

  return primQuantil, segQuantil, tercQuantil

print("\n==========================================")
print("------ MEDIDAS DE TENDÊNCIA CENTRAL ------")
print("Media Amostral: ", media_amostral(rows))
print("Mediana Amostral: ", mediana_amostral(rows))
print("Moda Amostral: ", moda_amostral(rows))
print("\n------     MEDIDAS DE DISPERSÃO     ------")
print("Vairancia Amostral: ", variancia_amostral(rows))
print("Desvio Padrão Amostral: ", desvio_padrao(variancia_amostral(rows)))
print("Desvio Médio Absoluto: ", desvio_medio_absoluto(rows))
print("\n------         SEPARATRIZES         ------")
print("Primeiro Quartil: ",qualtil(rows)[0])
print("Segundo  Quartil: ",qualtil(rows)[1])
print("Terceito Quartil: ",qualtil(rows)[2])
print("==========================================")

print("\nVALIDANDO COM AS FUNÇÕES ESTATÍSTICAS DO PYTHON")
print("Média: ", statistics.mean(rows))
print("Mediana: ", statistics.median(rows))
print("Moda: ", statistics.mode(rows))
print("-----------------")
print("Variancia: ", statistics.variance(rows))
print("Desvio Padrão: ", statistics.stdev(rows))
print("-----------------")

# print("\n",qualtil([1,2,3,4,5,6,7,8,9,10,11,12,13,13,13,30,31]))
# print("\n",qualtil([12,11,3,2,4,7,8,1,1,20,21,31,13,14,17,19,20]))
# print("\n[1 a  4] ->",qualtil([1,2,3,4]))
# print("[1 a  5] ->",qualtil([1,2,3,4,5]))
# print("[1 a  6] ->",qualtil([1,2,3,4,5,6]))
# print("[1 a  7] ->",qualtil([1,2,3,4,5,6,7]))
# print("[1 a  8] ->",qualtil([1,2,3,4,5,6,7,8]))
# print("[1 a  9] ->",qualtil([1,2,3,4,5,6,7,8,9]))
# print("[1 a 10] ->",qualtil([1,2,3,4,5,6,7,8,9,10]))
# print("[1 a 11] ->",qualtil([1,2,3,4,5,6,7,8,9,10,11]))
# print("[1 a 12] ->",qualtil([1,2,3,4,5,6,7,8,9,10,11,12]))
# print("[1 a 13] ->",qualtil([1,2,3,4,5,6,7,8,9,10,11,12,13]))
# print("[1 a 14] ->",qualtil([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
# print("[1 a 15] ->",qualtil([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
# print("[1 a 16] ->",qualtil([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
# print("[1 a 17] ->",qualtil([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]))
# print("[1 a 18] ->",qualtil([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]))