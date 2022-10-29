import matplotlib.pyplot as plt
import pandas as pd
import Tabele as T
import Wykresy as W

# wczytywanie danych z pliku
dane = pd.read_csv('kad.csv', header=None, names=["Długość działki kielicha", "Szerokość działki kielicha",
                                                  "Długość płatka", "Szerokość płatka", "ID"])
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

T.tabela1(tabela_ID_gatunkow)
T.tabela2(tabela_dlugosci_dzialki_kielicha,tabela_szerokosci_dzialki_kielicha,tabela_dlugosci_platka,tabela_szerokosci_platka)

W.wykresy(Dlug_dzial_kiel,Szer_dzial_kiel,Dlug_plat,Szer_plat,tabela_dlugosci_dzialki_kielicha,tabela_szerokosci_dzialki_kielicha,tabela_dlugosci_platka,tabela_szerokosci_platka)

plt.show()
