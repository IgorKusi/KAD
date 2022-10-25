import Func as F
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def tabela1(tabela_ID_gatunkow=None):
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

    # zmiana wielkosci obrazu
    plt.rcParams["figure.figsize"] = [3.00, 2.50]
    plt.rcParams["figure.autolayout"] = True

    tabela_licznosci, ax = plt.subplots()

    # pogrubiam krawędzie tabeli
    tabela_licznosci.patch.set_visible(False)

    # wyłączam widoczność osi
    ax.axis('off')

    # tablica "dane" to 2D list, array, zwał jak zwał w pytonie
    # ktorej pierwszy wymiar musi sie zgadzac z iloscia kolumn
    # ktorych naglowki zadeklarowane sa dalej jako "kolumny"
    dane = [["Setosa", str(populacja_Gat1) + "(" + str(round(populacja_Gat1 / populacjaIrysow * 100, 1)).replace(".",",") + "%)"],
            ["Versicolor", str(populacja_Gat2) + "(" + str(round(populacja_Gat2 / populacjaIrysow * 100, 1)).replace(".",",") + "%)"],
            ["Virginica", str(populacja_Gat3) + "(" + str(round(populacja_Gat3 / populacjaIrysow * 100, 1)).replace(".",",") + "%)"]]

    kolumny = ["Gatunek", "Liczebność(%)"]

    # przy uzyciu DataFrame mozna ladnie i bezbolesnie
    # przeniesc te wszystkie dane bezposrednio do tabeli
    df = pd.DataFrame(dane, columns=kolumny)
    ax = plt.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center', colWidths=[0.3, 0.3])

    #rozmiar czcionki
    ax.auto_set_font_size(False)
    ax.set_fontsize(7)

    tabela_licznosci.tight_layout()
    plt.savefig('Tabela1.pdf')
    #plt.show()

    return

def tabela2(tab_dl_kiel=None, tab_sz_kiel=None, tab_dl_plat=None, tab_sz_plat=None):

    #Skalowanie wielkosci obrazu
    plt.rcParams["figure.figsize"] = [12.00,2.50]
    #plt.rcParams["figure.autolayout"] = True
    if tab_sz_plat is None:
        tab_sz_plat = []
    if tab_dl_plat is None:
        tab_dl_plat = []
    if tab_sz_kiel is None:
        tab_sz_kiel = []
    if tab_dl_kiel is None:
        tab_dl_kiel = []
    tabela, ax = plt.subplots()

    # pogrubiam krawędzie tabeli
    tabela.patch.set_visible(False)

    # wyłączam widoczność osi
    ax.axis('off')


    kolumny = ["Cecha", "Minimum", "Śr.arytm(+- odch.stand.)", "Mediana (Q1-Q3)", "Maksimum"]


# dlaczego taki syf? gdyż ponieważ należy formatować liczby zgodnie z polska notacją
# czyli we floatach nie "." tylko ","  ( .replace(".",",") )
# poza tym, kazda wartosc musi byc wypisywana z dokladnie 2 miejscami po przecinku ("{:.2f}".format())
    dane = [["Długość działki kielicha (cm)",
              str(F.mini(tab_dl_kiel)).replace(".", ","),
              str("{:.2f}".format(F.srednia_aryt(tab_dl_kiel))).replace(".",",") + "(+-" + str(F.odch_stand(tab_dl_kiel)).replace(".",",") + ")",
              str("{:.2f}".format(F.mediana(tab_dl_kiel))).replace(".",",")+"("+str("{:.2f}".format(F.kwartyl(tab_dl_kiel, 1))).replace(".",",")+"-"+str("{:.2f}".format(F.kwartyl(tab_dl_kiel,3))).replace(".",",")+")",
              str(F.maks(tab_dl_kiel)).replace(".", ",")],

             ["Szerekość działki kielicha (cm)",
              str(F.mini(tab_sz_kiel)).replace(".", ","),
              str("{:.2f}".format(F.srednia_aryt(tab_sz_kiel))).replace(".",",")+"(+-"+str(F.odch_stand(tab_sz_kiel)).replace(".",",")+")",
              str("{:.2f}".format(F.mediana(tab_sz_kiel))).replace(".",",")+"("+str("{:.2f}".format(F.kwartyl(tab_sz_kiel, 1))).replace(".",",")+"-"+str("{:.2f}".format(F.kwartyl(tab_sz_kiel,3))).replace(".",",")+")",
              str(F.maks(tab_sz_kiel)).replace(".", ",")],

             ["Długość płatka (cm)",
              str(F.mini(tab_dl_plat)).replace(".", ","),
              str("{:.2f}".format(F.srednia_aryt(tab_dl_plat))).replace(".",",")+"(+-"+str(F.odch_stand(tab_dl_plat)).replace(".",",")+")",
              str("{:.2f}".format(F.mediana(tab_dl_plat))).replace(".",",")+"("+str("{:.2f}".format(F.kwartyl(tab_dl_plat, 1))).replace(".",",")+"-"+str("{:.2f}".format(F.kwartyl(tab_dl_plat,3))).replace(".",",")+")",
              str(F.maks(tab_dl_plat)).replace(".", ",")],

             ["Szerekość płatka (cm)",
              str(F.mini(tab_sz_plat)).replace(".", ","),
              str("{:.2f}".format(F.srednia_aryt(tab_sz_plat))).replace(".",",")+"(+-"+str(F.odch_stand(tab_sz_plat)).replace(".",",")+")",
              str("{:.2f}".format(F.mediana(tab_sz_plat))).replace(".",",")+"("+str("{:.2f}".format(F.kwartyl(tab_sz_plat, 1))).replace(".",",")+"-"+str("{:.2f}".format(F.kwartyl(tab_sz_plat,3))).replace(".",",")+")",
              str(F.maks(tab_sz_plat)).replace(".", ",")]]

    df=pd.DataFrame(dane, columns=kolumny)

    ax = plt.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center', colWidths=[0.30,0.12,0.22,0.15,0.1])

    #zmiana wielkosci czcionki
    ax.auto_set_font_size(False)
    ax.set_fontsize(10)

    tabela.tight_layout()
    plt.savefig('Tabela2.pdf')
    #plt.show()

    return
