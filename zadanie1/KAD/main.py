import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import Func as f

# wczytywanie danych z pliku
dane = pd.read_csv('kad.csv', header=None, names=["DP", "SP", "DK", "SK", "ID"])
Dlug_plat = pd.read_csv(r'kad.csv',header=None, usecols=[0])
Szer_plat = pd.read_csv(r'kad.csv', header=None, usecols=[1])
Dlug_kiel = pd.read_csv(r'kad.csv', header=None, usecols=[2])
Szer_kiel = pd.read_csv(r'kad.csv', header=None, usecols=[3])
ID_Gat = pd.read_csv(r'kad.csv',header=None, usecols=[4])

# tablica z wartosciami długosci płatków
tabela_dlugosci_platkow = Dlug_plat.squeeze()

# tabliza w wartościami szerokości płatków
tabela_szerokosci_platkow = Szer_plat.squeeze()

# tablica z wartościami długości kielicha
tabela_dlugosci_kielicha = Dlug_kiel.squeeze()

# tablica z wartościami szerokości kielicha
tabela_szerokosci_kielicha = Szer_kiel.squeeze()

# tablica z indeksami gatunków
tabela_ID_gatunkow = ID_Gat.squeeze()

f.wyznacz_licznosc(tabela_ID_gatunkow)

print("Badanie dlugosci platkow" '\n')
f.wyznacz_max_min(tabela_dlugosci_platkow)

print("Badanie szerokosci platkow" '\n')
f.wyznacz_max_min(tabela_szerokosci_platkow)

print("Badanie dlugosci kielicha" '\n')
f.wyznacz_max_min(tabela_dlugosci_kielicha)

print("Badanie szerokosci kielicha" '\n')
f.wyznacz_max_min(tabela_szerokosci_kielicha)
