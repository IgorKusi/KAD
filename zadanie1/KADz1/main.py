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

# tablica z wartosciami długosci płatków
tabela_dlugosci_dzialki_kielicha = Dlug_dzial_kiel.squeeze()

# tabliza w wartościami szerokości płatków
tabela_szerokosci_dzialki_kielicha = Szer_dzial_kiel.squeeze()

# tablica z wartościami długości kielicha
tabela_dlugosci_platka = Dlug_plat.squeeze()

# tablica z wartościami szerokości kielicha
tabela_szerokosci_platka = Szer_plat.squeeze()

# tablica z indeksami gatunków
tabela_ID_gatunkow = ID_Gat.squeeze()

tab = [1,2,3,4,5,6,7,7,7,7]

f.wyznacz_licznosc(tabela_ID_gatunkow)
print(f.srednia_aryt(tabela_dlugosci_platka))
print(f.odch_stand(tabela_dlugosci_platka))
print(f.srednia_aryt(tab))
print(f.odch_stand(tab))
print(f.mediana(tab))
print(f.srednia_aryt(tabela_dlugosci_dzialki_kielicha))
print(f.odch_stand(tabela_dlugosci_dzialki_kielicha))