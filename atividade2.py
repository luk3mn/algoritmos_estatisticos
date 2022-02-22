# Exemplo 7.4
# Ao invés de um grupo de cinco pessoas, como no exemplo 7.3, consideremos 
# agora as seis seguintes estaturas: 1,85m; 1,60m; 1,70m; 1,65m; 1,60m e 
# 1,62m. Assim, Emd= N/2 = 6/2 = 3. Colocando os valores em ordem crescente: 
# 1,60; 1,60; 1,62; 1,65; 1,70; 1,85, obtemos que 1,62 e 1,65 são os dois 
# valores centrais. Logo:

rows = [1.85, 1.60, 1.70, 1.65, 1.60, 1.62]

def mediana_amostral(dados):
  dados.sort()
  # calculo da mediana amostral
  for i in range(len(dados)):
    if len(dados) % 2 == 0: # se n for par
      index = int((len(dados) / 2))
      med = (dados[index] + dados[index-1])/2 # calcula a mediana se n for par
    else: # se n for impar
      index = int((len(dados)+1) / 2)
      med = dados[index-1] # calcula a mediana se n for impar
  return med

print("\n==============================")
print(" | Mediana amostral: ", mediana_amostral(rows), "|") # 1.635
print("==============================")
