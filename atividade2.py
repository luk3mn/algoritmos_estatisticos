# Suponha que 20 alunos responderam quatões conforme o row das notas de 4 a 8
# 7 6 7 6 7
# 4 5 7 5 8
# 6 5 5 7 8
# 4 7 7 7 6
import statistics

rows = [7, 6, 7, 6, 7, 4, 5, 7, 5, 8, 6, 5, 5, 7, 8, 4, 7, 7, 7, 6]
rows.sort()


def mediana_amostral(dados):
    amostra = []
    frequencia = []
    for dado in dados:
        if dado in amostra:
            pass
        else:
            amostra.append(dado)
            frequencia.append(dados.count(dado))

    fx = []
    for i in range(len(amostra)):
        aux = amostra[i] * frequencia[i]
        fx.append(aux)

    fx.sort()
    # calculo da mediana amostral
    for i in range(len(fx)):
        if len(fx) % 2 == 0:
            index = int((len(fx) / 2) - 0.5)
            med = fx[index] + 0.5
        else:
            index = int((len(fx) / 2) - 0.5)
            med = fx[index]

    return amostra, frequencia, fx, med


print("\n==============================")
print(" | x: ", mediana_amostral(rows)[0], "      |")
print(" | f: ", mediana_amostral(rows)[1], "      |")
print(" | fx:", mediana_amostral(rows)[2], "  |")
print(" | Mediana amostral: ", mediana_amostral(rows)[3]) # 20
print("==============================")
