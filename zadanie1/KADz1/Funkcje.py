import numpy as np


def sortuj_rosnaco(tabela_danych=None):
    if tabela_danych is None:
        tabela_danych = []
    n = len(tabela_danych)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if tabela_danych[j] > tabela_danych[j + 1]:
                tabela_danych[j], tabela_danych[j + 1] = tabela_danych[j + 1], tabela_danych[j]

    return

# funkcja zwracająca najwiekszy element zbioru danych
def maks(tabela_danych=None):
    if tabela_danych is None:
        tabela_danych = []
    maks = 0.0
    for i in range(len(tabela_danych)):
        if tabela_danych[i] > maks:
            maks = tabela_danych[i]
    return "{:.2f}".format(maks)


# funkcja zwracająca najmniejszy element zbioru danych
def mini(tabela_danych=None):
    if tabela_danych is None:
        tabela_danych = []
    mini = 9999.0
    for i in range(len(tabela_danych)):
        if tabela_danych[i] < mini:
            mini = tabela_danych[i]
    return "{:.2f}".format(mini)


# funkcja zwracajaca średnia arytmetyczna zbioru danych
def srednia_aryt(tabela_danych=None):
    if tabela_danych is None:
        tabela_danych = []

    suma, licznik = 0, 0

    for i in range(len(tabela_danych)):
        licznik = licznik+1
        suma = suma+tabela_danych[i]

    return round(suma/licznik, 2)


# funckja zwracająca mediane zbioru danych
def mediana(tabela_danych=None):

    if tabela_danych is None:
        tabela_danych = []

    sortuj_rosnaco(tabela_danych)

    if len(tabela_danych)%2 == 1:
        return round(tabela_danych[int(len(tabela_danych)/2)-1], 2)

    else:
        srodkowe_liczby = [tabela_danych[int(len(tabela_danych)/2)-1], tabela_danych[int(len(tabela_danych)/2)]]
        return round(srednia_aryt(srodkowe_liczby), 2)


# funkcja zwracająca wartość odchylenia standardowego zbioru danych
def odch_stand(tabela_danych=None):
    if tabela_danych is None:
        tabela_danych = []

    srednia=srednia_aryt(tabela_danych)
    wariancja = 0

    for i in range(len(tabela_danych)):
        wariancja=wariancja+((tabela_danych[i]-srednia)*(tabela_danych[i]-srednia))

    wariancja=wariancja/len(tabela_danych)

    return "{:.2f}".format(round(np.sqrt(wariancja),2))


# funkcja zwracajaca wartosc danego kwartyla zbioru danych
# parametr 'numer' oznacza ktory kwartyl chcemy obliczyc, domyslnie 1
def kwartyl(tabela_danych=None, numer=1):
    if tabela_danych is None:
        tabela_danych = []

    sortuj_rosnaco(tabela_danych)

    med = mediana(tabela_danych)

    if numer == 1:
        mn_od_med = []
        for i in range(int((len(tabela_danych)/2)+1)):
            if tabela_danych[i] < med:
                mn_od_med.append(tabela_danych[i])
        return mediana(mn_od_med)
    elif numer == 2:
        return med

    elif numer == 3:
        wieksze_od_med = []
        for i in range(int((len(tabela_danych))/2)-1,int((len(tabela_danych)))-1):
            if tabela_danych[i] > med:
                wieksze_od_med.append(tabela_danych[i])
        return mediana(wieksze_od_med)







