# Exemplo 6.3 - pág 134 do livro "Introdução a estatística"
# Os dados seguintes são os rendimentos de 70 examinandos numa 
# prova de raciocínio:
# 25 42 26 25 42 23 41 22 43 20 28 39
# 30 29 38 29 37 28 40 28 31 35 32 31
# 35 31 34 32 36 31 33 43 34 33 33 32
# 34 34 32 34 35 32 34 36 32 35 31 36
# 32 34 37 30 39 40 30 38 30 40 31 37
# 41 23 40 26 41 27 43 28 38 41
from statistics import mean


rows = [25, 42, 26, 25, 42, 23, 41, 22, 43, 20, 28, 39, 30, 29, 38, 29, 37,
        28, 40, 28, 31, 35, 32, 31, 35, 31, 34, 32, 36, 31, 33, 43, 34, 33,
        33, 32, 34, 34, 32, 34, 35, 32, 34, 36, 32, 35, 31, 36, 32, 34, 37,
        30, 39, 40, 30, 38, 30, 40, 31, 37, 41, 23, 40, 26, 41, 27, 43, 28,
        38, 41]
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
print("x: ", media_amostral(rows)[0]) # vai imprimir os valores agrupados
print("f: ", media_amostral(rows)[1]) # vai imprimir a frequencia dos valroes agrupados
print("Media amostral: ", media_amostral(rows)[2])  # 33,46
print("==============================")
