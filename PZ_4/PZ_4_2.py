# Дано целое число N (>0), являющееся некоторой степенью числа 2: N = 2^K.
# Найти целое число K — показатель этой степени.
import math

try:

    N = int(input('Целое число N (>0): '))
    if N > 0:
        K = int(math.log(N, 2))
    else:
        exit()
    print('Показатель степени K:', K)

except:
    print('False')
