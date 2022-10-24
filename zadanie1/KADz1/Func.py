import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def wyznacz_licznosc(tabela_ID_gatunkow=None):

    if tabela_ID_gatunkow is None:
        tabela_ID_gatunkow = []

    populacja_Gat1 = 0
    populacja_Gat2 = 0
    populacja_Gat3 = 0

    # Pętla zliczająca populacje poszczególnych gatunków
    for i in range(len(tabela_ID_gatunkow)):
        if tabela_ID_gatunkow[i] == 0:
            populacja_Gat1 = populacja_Gat1+1
        if tabela_ID_gatunkow[i] == 1:
            populacja_Gat2 = populacja_Gat2+1
        if tabela_ID_gatunkow[i] == 2:
            populacja_Gat3 = populacja_Gat3+1

    populacjaIrysow = len(tabela_ID_gatunkow)


    tabela_licznosci, ax =  plt.subplots()

    # pogrubiam krawędzie tabeli
    tabela_licznosci.patch.set_visible(False)

    # wyłączam widoczność osi
    ax.axis('off')

    dane = [["Setosa", str(populacja_Gat1) + "(" + str(round(populacja_Gat1/populacjaIrysow*100,1))+"%)"],
            ["Versicolor", str(populacja_Gat2) + "(" + str(round(populacja_Gat2/populacjaIrysow*100, 1))+"%)"],
            ["Virginica",str(populacja_Gat3) + "(" + str(round(populacja_Gat3/populacjaIrysow*100, 1))+"%)"]]

    kolumny=["Gatunek", "Liczebność(%)"]

    df = pd.DataFrame(dane,columns=kolumny)

    # TODO nie wiem jak zrobic zeby tabela sie rozciągała na cały obraz,  dokumentacja za duzo o tym nie mowi

    ax = plt.table(cellText=df.values, colLabels=df.columns, loc='center',cellLoc='center', colWidths=[0.3,0.3])
    tabela_licznosci.tight_layout()
    plt.show()

    return


def wyznacz_max(tabela_danych=None):
    if tabela_danych is None:
        tabela_danych = []
    maks = 0.0
    for i in range(len(tabela_danych)):
        if tabela_danych[i] > maks:
            maks = tabela_danych[i]
    return maks


def wyznacz_min(tabela_danych=None):
    if tabela_danych is None:
        tabela_danych = []
    mini = 9999.0
    for i in range(len(tabela_danych)):
        if tabela_danych[i] > mini:
            mini = tabela_danych[i]
    return mini
