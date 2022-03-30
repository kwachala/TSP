import numpy as np
import random
from collections import Counter


def PK_SW(macierz):
    trasa = random.sample(range(0, len(macierz)), len(macierz))
    for i in range(len(trasa)):
        if trasa[i] == len(macierz) - 1:
            trasa[i], trasa[0] = trasa[0], trasa[i]

    Td = czas(macierz, trasa)
    iteracje = 1
    T_0 = 80
    T = T_0

    print('------------------------------------------------------------------------')
    print('[ 0 ]', 'Początkowa trasa: ', trasa, 'Td: ', Td)
    print('------------------------------------------------------------------------')

    while iteracje <= 150:

        n = random.sample(range(1, len(macierz)), 2)

        trasa1 = swap(trasa, n[1], n[0])

        Td1 = czas(macierz, trasa1)

        trasaa = trasa1
        tdd = Td1

        if Td1 < Td:
            trasa, Td = trasa1, Td1
        else:
            rand = np.random.uniform()
            if rand <= np.exp(-(Td1 - Td) / T):
                trasa, Td = trasa1, Td1

        T = T * 0.8

        print('[', iteracje, ']', 'Trasa:', trasaa, 'Td =', tdd, ',', 'Trasa*: ', trasa, 'Td* =', Td)
        print('------------------------------------------------------------------------')
        iteracje += 1

    return trasa, Td


def swap(trasa, m, n):
    i, j = min(m, n), max(m, n)
    trasa1 = trasa.copy()
    while i < j:
        trasa1[i], trasa1[j] = trasa1[j], trasa1[i]
        i += 1
        j -= 1
    return trasa1


def czas(macierz, trasa):
    l = 0
    for i in range(len(trasa) - 1):
        l += macierz[trasa[i]][trasa[i + 1]]
    l += macierz[trasa[len(trasa) - 1]][trasa[0]]
    return l


macierz_czasu = [[0, 2, 4, 3],
                 [2, 0, 3, 5],
                 [4, 3, 0, 6],
                 [3, 5, 6, 0]]

PK_SW(macierz_czasu)

"""
test = []
for i in range(100):
    trasa = PK_SW(macierz_czasu)[1]
    print(trasa)
    test.append(trasa)

print(Counter(test))
"""
