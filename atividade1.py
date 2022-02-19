# Suponha que 20 alunos responderam quatões conforme o row das notas de 4 a 8
# 7 6 7 6 7
# 4 5 7 5 8
# 6 5 5 7 8
# 4 7 7 7 6

rows = [7, 6, 7, 6, 7, 4, 5, 7, 5, 8, 6, 5, 5, 7, 8, 4, 7, 7, 7, 6]
rows.sort()


def media_amostral(dados):
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
    # formula da média amostral
    mediaAmostral = sum(fx) / sum(frequencia)
    return amostra, frequencia, round(mediaAmostral, 2)


print("\n==============================")
print(" | x: ", media_amostral(rows)[0], "      |")
print(" | f: ", media_amostral(rows)[1], "      |")
print(" | Media amostral: ", media_amostral(rows)[2], "     |")  # 6,2
print("==============================")
