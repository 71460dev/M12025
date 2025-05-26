# 1. Importar o módulo statistics e criar uma lista com 14 números em ordem crescente
import statistics

elem_14 = [1, 2, 3, 10, 11, 12, 13, 14, 15, 16, 17, 40, 41, 42]

# 2. Calcule a média e a mediana dos valores usando o módulo completo (import statistics)
media1 = statistics.mean(elem_14)
mediana1 = statistics.median(elem_14)
print("Média (uso completo):", media1)
print("Mediana (uso completo):", mediana1)

# 3. Use um alias (apelido) para o módulo statistics e refaça os cálculos. Dica: import statistics as st
import statistics as st

media2 = st.mean(elem_14)
mediana2 = st.median(elem_14)
print("Média (com alias):", media2)
print("Mediana (com alias):", mediana2)

# 4. Agora, importe apenas as funções mean e median do módulo statistics e refaça os cálculos.
from statistics import mean, median

media3 = mean(elem_14)
mediana3 = median(elem_14)
print("Média (importação direta):", media3)
print("Mediana (importação direta):", mediana3)

# 5. Por fim, importe todas as funções do módulo statistics e calcule novamente a média e a mediana da lista.
from statistics import *

media4 = mean(elem_14)
mediana4 = median(elem_14)
print("Média (importação de tudo):", media4)
print("Mediana (importação de tudo):", mediana4)