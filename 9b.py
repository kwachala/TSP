import random
import numpy as np


def PK_SW(los_rozwiazanie):
    rozwiazanie = los_rozwiazanie
    iteracje = 1
    T_0 = 80
    T = T_0

    print('------------------------------------------------------------------------------------------------------------------------------------------------')
    print('[ 0 ]', 'Początkowa trasa i podział produkcji: ', rozwiazanie, 'Td+Tp: ', oblicz_czas(rozwiazanie))
    print('------------------------------------------------------------------------------------------------------------------------------------------------')

    while iteracje <= 150:
        sasiad = znajdz_sasiada(rozwiazanie)

        if oblicz_czas(rozwiazanie) > oblicz_czas(sasiad):
            rozwiazanie = sasiad
        else:
            if random.uniform(0, 1) < np.exp(oblicz_czas(rozwiazanie) - oblicz_czas(sasiad) / T):
                rozwiazanie = sasiad

        T = T * 0.8

        print('[', iteracje, ']', 'Trasa i podział produkcji:', sasiad, 'Td+Tp = ', oblicz_czas(sasiad))
        print('      Trasa i podział produkcji*: ', rozwiazanie, 'Td+Tp* = ', oblicz_czas(rozwiazanie))
        print('------------------------------------------------------------------------------------------------------------------------------------------------')

        iteracje += 1

    return rozwiazanie


def oblicz_czas(rozwiazanie):
    macierz_czasu = [[0, 2, 4, 3],
                     [2, 0, 3, 5],
                     [4, 3, 0, 6],
                     [3, 5, 6, 0]]

    U = [2, 3, 4]

    [trasa0, trasa1, trasa2] = rozwiazanie[0]
    [P0, P1, P2] = rozwiazanie[1]

    Tp = [P0 / U[0], P1 / U[1], P2 / U[2]]

    TdTp = 0
    TdTp += max(TdTp + macierz_czasu[3][trasa0], Tp[trasa0])
    TdTp = max(TdTp + macierz_czasu[trasa0][trasa1], Tp[trasa1])
    TdTp = max(TdTp + macierz_czasu[trasa1][trasa2], Tp[trasa2])
    TdTp += macierz_czasu[trasa2][3]

    return TdTp


def znajdz_sasiada(rozwiazanie):
    trasa, produkcja = rozwiazanie[0], rozwiazanie[1]
    nowa_trasa, nowa_produkcja = znajdz_sasiada_trasa(trasa), znajdz_sasiada_produkcja(produkcja, 8)

    sasiedzi = []
    sasiedzi.append([nowa_trasa, nowa_produkcja])
    sasiedzi.append([trasa, nowa_produkcja])
    sasiedzi.append([nowa_trasa, produkcja])

    sasiad = random.choice(sasiedzi)

    return sasiad


def podzial_produkcji():
    suma = 66
    [k_p1, k_p2, k_p3] = [random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10)]
    k_suma = k_p1 + k_p2 + k_p3
    K = suma / k_suma
    P1, P2, P3 = k_p1 * K, k_p2 * K, k_p3 * K
    return [P1, P2, P3]


def roznica_produkcji(produkcja1, produkcja2):
    roznica = 0
    for i in range(len(produkcja1)):
        roznica += np.abs(produkcja1[i] - produkcja2[i])

    return roznica


def znajdz_sasiada_produkcja(produkcja, n):
    lista_sasiadow = []
    lista_roznic = []
    for i in range(n):
        lista_sasiadow.append(podzial_produkcji())
        lista_roznic.append(roznica_produkcji(produkcja, lista_sasiadow[-1]))

    min_roznica = 100
    for i in range(n):
        if lista_roznic[i] < min_roznica:
            min_roznica = lista_roznic[i]
            sasiad = lista_sasiadow[i]

    return sasiad


def znajdz_sasiada_trasa(trasa):
    n, m = random.sample(range(0, len(trasa)), 2)

    i, j = min(m, n), max(m, n)
    sasiad = trasa.copy()
    while i < j:
        sasiad[i], sasiad[j] = sasiad[j], sasiad[i]
        i += 1
        j -= 1

    return sasiad


"""
def test(n):
    y = []
    x = []
    for i in range(n):
        los_trasa = random.sample([0, 1, 2], 3)
        los_produkcja = podzial_produkcji()
        rozwiazanie = PK_SW([los_trasa, los_produkcja])
        y.append(oblicz_czas(rozwiazanie))
        x.append(i)

    licz_14 = 0
    for i in y:
        if i == 14:
            licz_14 += 1

    return licz_14 / n * 100

print("Procent dobrych rozwiązań = ", test(100), "%")

"""

los_trasa = random.sample([0, 1, 2], 3)
los_produkcja = podzial_produkcji()
PK_SW([los_trasa, los_produkcja])
