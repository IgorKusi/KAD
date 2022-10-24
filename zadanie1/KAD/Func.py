import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def wyznacz_licznosc(tabela_ID_gatunkow=None):

    if tabela_ID_gatunkow is None:
        tabela_ID_gatunkow = []
    populacja_Gat1 = 0
    populacja_Gat2 = 0
    populacja_Gat3 = 0
    for i in range(len(tabela_ID_gatunkow)):
        if tabela_ID_gatunkow[i] == 0:
            populacja_Gat1 = populacja_Gat1+1
        if tabela_ID_gatunkow[i] == 1:
            populacja_Gat2 = populacja_Gat2+1
        if tabela_ID_gatunkow[i] == 2:
            populacja_Gat3 = populacja_Gat3+1

    print("Populacja gatunku Setosa: ", populacja_Gat1, '\n'
          "Populacja gatunku Versicolor: ", populacja_Gat2, '\n'
          "Populacja gatunku Virginica: ", populacja_Gat3, '\n')

    populacjaIrysow= len(tabela_ID_gatunkow)

    print("Procentowy udział gatunku Setosa w populacji irysów: ", round((populacja_Gat1/populacjaIrysow)*100, 2), "%" '\n'
          "Procentowy udział gatunku Versicolor w populacji irysów: ", round((populacja_Gat2/populacjaIrysow)*100, 2), "%"'\n'
          "Procentowy udział gatunku Virginica w populacji irysów: ", round((populacja_Gat2/populacjaIrysow)*100, 2), "%"'\n')
    return


def wyznacz_max_min(tabela_danych=None):
    if tabela_danych is None:
        tabela_danych = []
    maks = 0.0
    mini = 1000.0
    for i in range(len(tabela_danych)):
        if tabela_danych[i] > maks:
            maks = tabela_danych[i]
        if tabela_danych[i] < mini:
            mini = tabela_danych[i]

    print("Największa wartość badanej cechy: ", maks, '\n'
          "Najmniejsza wartość badanej cechy: ", mini, '\n\n')
    return

