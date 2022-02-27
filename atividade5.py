# Uma organização de educação de consumidores afirma que há uma diferença entre a média
# da dívida do cartão de crédito de homens e mulheres. Sabe-se, de estudos anteriores, que o
# desvio padrão para a dívida das mulheres é de $ 750 e, dos homens, $ 800. Os resultados de
# uma pesquisa aleatória de 200 indivíduos de cada grupo foram: média da dívida das mulheres:
# $ 2.290; média da dívida dos homens: $ 2.370. Verifique se, ao nível de 5%, a afirmação da
# organização está correta.

from math import sqrt
from statistics import mean, stdev

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