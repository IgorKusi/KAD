import matplotlib.pyplot as plt
import pandas as pd
import Func as F
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

# _______________________________________________________________
# TODO przerobić to z maina na funkcje w pliku Wykresy.py
# TODO dodać podpisy osi
# TODO wykresy pudełkowe
# TODO poprawić czytelność histogramów

plt.rcParams["figure.figsize"] = [10.00, 20.00]
fig,ax = plt.subplots(4, 2, tight_layout=True)

ax[0][0].hist(Dlug_dzial_kiel, bins=8)
ax[0][0].set_title("Długość działki kielicha")

ax[1][0].hist(Szer_dzial_kiel, bins=8)
ax[1][0].set_title("Szerokość działki kielicha")

ax[2][0].hist(Dlug_plat, bins=8)
ax[2][0].set_title("Długość płatka")

ax[3][0].hist(Szer_plat, bins=8)
ax[3][0].set_title("Szerokośc płatka")
plt.savefig("Wykresy.pdf")
plt.show()
