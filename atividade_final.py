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
print("Quartil: ")
print("==========================================")

print("\nVALIDANDO COM AS FUNÇÕES ESTATÍSTICAS DO PYTHON")
print("Média: ", statistics.mean(rows))
print("Mediana: ", statistics.median(rows))
print("Moda: ", statistics.mode(rows))
print("-----------------")
print("Variancia: ", statistics.variance(rows))
print("Desvio Padrão: ", statistics.stdev(rows))
print("-----------------")
