import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# bubble sort
# za wszystkie krzywdy sam przeprosze Boga
def sortuj_rosnaco(tabela_danych=None):
    if tabela_danych is None:
        tabela_danych = []
    n = len(tabela_danych)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if tabela_danych[j] > tabela_danych[j + 1]:
                tabela_danych[j], tabela_danych[j + 1] = tabela_danych[j + 1], tabela_danych[j]

    return


def wyznacz_licznosc(tabela_ID_gatunkow=None):
    if tabela_ID_gatunkow is None:
        tabela_ID_gatunkow = []

    populacja_Gat1 = 0
    populacja_Gat2 = 0
    populacja_Gat3 = 0

    # Pętla zliczająca populacje poszczególnych gatunków
    for i in range(len(tabela_ID_gatunkow)):
        if tabela_ID_gatunkow[i] == 0:
            populacja_Gat1 = populacja_Gat1 + 1
        if tabela_ID_gatunkow[i] == 1:
            populacja_Gat2 = populacja_Gat2 + 1
        if tabela_ID_gatunkow[i] == 2:
            populacja_Gat3 = populacja_Gat3 + 1

    populacjaIrysow = len(tabela_ID_gatunkow)

    tabela_licznosci, ax = plt.subplots()

    # pogrubiam krawędzie tabeli
    tabela_licznosci.patch.set_visible(False)

    # wyłączam widoczność osi
    ax.axis('off')

    dane = [["Setosa", str(populacja_Gat1) + "(" + str(round(populacja_Gat1 / populacjaIrysow * 100, 1)) + "%)"],
            ["Versicolor", str(populacja_Gat2) + "(" + str(round(populacja_Gat2 / populacjaIrysow * 100, 1)) + "%)"],
            ["Virginica", str(populacja_Gat3) + "(" + str(round(populacja_Gat3 / populacjaIrysow * 100, 1)) + "%)"]]

    kolumny = ["Gatunek", "Liczebność(%)"]

    df = pd.DataFrame(dane, columns=kolumny)

    # TODO nie wiem jak zrobic zeby tabela sie rozciągała na cały obraz,  dokumentacja za duzo o tym nie mowi

    ax = plt.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center', colWidths=[0.3, 0.3])
    tabela_licznosci.tight_layout()
    plt.show()

    return


def maks(tabela_danych=None):
    if tabela_danych is None:
        tabela_danych = []
    maks = 0.0
    for i in range(len(tabela_danych)):
        if tabela_danych[i] > maks:
            maks = tabela_danych[i]
    return maks


def mini(tabela_danych=None):
    if tabela_danych is None:
        tabela_danych = []
    mini = 9999.0
    for i in range(len(tabela_danych)):
        if tabela_danych[i] > mini:
            mini = tabela_danych[i]
    return mini


def srednia_aryt(tabela_danych=None):
    if tabela_danych is None:
        tabela_danych = []

    suma, licznik = 0, 0

    for i in range(len(tabela_danych)):
        licznik = licznik+1
        suma = suma+tabela_danych[i]

    return round(suma/licznik, 2)


def mediana(tabela_danych=None):

    if tabela_danych is None:
        tabela_danych = []

    sortuj_rosnaco(tabela_danych)

    # TODO  NIE MAM POJECIA DLACZEGO TO WYWALA INDEX OUT OF RANGE ALE NIE WYTRZYMAM ZARAZ
    if len(tabela_danych)%2 == 0:
        wynik = round(tabela_danych[int(len(tabela_danych)/2)-1], 2)
        return wynik

    else:
        srodkowe_liczby = [tabela_danych[int(len(tabela_danych)/2)-1], tabela_danych[int(len(tabela_danych)/2)]]
        return round(srednia_aryt(srodkowe_liczby), 2)

def odch_stand(tabela_danych=None):
    if tabela_danych is None:
        tabela_danych = []

    srednia=srednia_aryt(tabela_danych)
    wariancja = 0

    for i in range(len(tabela_danych)):
        wariancja=wariancja+((tabela_danych[i]-srednia)*(tabela_danych[i]-srednia))

    wariancja=wariancja/len(tabela_danych)

    return np.sqrt(wariancja)


# parametr numer oznacza ktory kwartyl chcemy obliczyc, domyslnie 1
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




