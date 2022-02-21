# Suponhamos que os números de questões respondidas corretamente 
# por 20 alunos de psicologia em uma prova de estatística foram 
# os seguintes:
# 7 6 7 6 7
# 4 5 7 5 8
# 6 5 5 7 8
# 4 7 7 7 6
rows = [7, 6, 7, 6, 7, 4, 5, 7, 5, 8, 6, 5, 5, 7, 8, 4, 7, 7, 7, 6]

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

print("\n==============================")
print(" | Mediana amostral: ", mediana_amostral(rows), "   |") # 6.5
print("==============================")
