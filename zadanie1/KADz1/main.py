import matplotlib.pyplot as plt
import pandas as pd
import Func as f

# wczytywanie danych z pliku
dane = pd.read_csv('kad.csv', header=None, names=["DP", "SP", "DK", "SK", "ID"])
Dlug_dzial_kiel = pd.read_csv(r'kad.csv', header=None, usecols=[0])
Szer_dzial_kiel = pd.read_csv(r'kad.csv', header=None, usecols=[1])
Dlug_plat = pd.read_csv(r'kad.csv', header=None, usecols=[2])
Szer_plat = pd.read_csv(r'kad.csv', header=None, usecols=[3])
ID_Gat = pd.read_csv(r'kad.csv', header=None, usecols=[4])


tabela_dlugosci_dzialki_kielicha = Dlug_dzial_kiel.squeeze()

tabela_szerokosci_dzialki_kielicha = Szer_dzial_kiel.squeeze()

tabela_dlugosci_platka = Dlug_plat.squeeze()

tabela_szerokosci_platka = Szer_plat.squeeze()

tabela_ID_gatunkow = ID_Gat.squeeze()

# ________________________________________________________________

f.wyznacz_licznosc(tabela_ID_gatunkow)
f.generuj_tabele_2(tabela_dlugosci_dzialki_kielicha,tabela_szerokosci_dzialki_kielicha,tabela_dlugosci_platka,tabela_szerokosci_platka)