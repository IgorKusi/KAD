import matplotlib.pyplot as plt


# funkcja generująca wykresy pudełkowe oraz histogramy
def wykresy(Dlug_dzial_kiel=None, Szer_dzial_kiel=None, Dlug_plat=None, Szer_plat=None,
            tabela_dlugosci_dzialki_kielicha=None, tabela_szerokosci_dzialki_kielicha=None, tabela_dlugosci_platka=None,
            tabela_szerokosci_platka=None):
    if tabela_szerokosci_platka is None:
        tabela_szerokosci_platka = []
    if tabela_dlugosci_platka is None:
        tabela_dlugosci_platka = []
    if tabela_szerokosci_dzialki_kielicha is None:
        tabela_szerokosci_dzialki_kielicha = []
    if tabela_dlugosci_dzialki_kielicha is None:
        tabela_dlugosci_dzialki_kielicha = []
    if Szer_plat is None:
        Szer_plat = []
    if Dlug_plat is None:
        Dlug_plat = []
    if Szer_dzial_kiel is None:
        Szer_dzial_kiel = []
    if Dlug_dzial_kiel is None:
        Dlug_dzial_kiel = []

    # ustalam rozmiar okna na ktorym będą wyświetlane wykresy
    plt.rcParams["figure.figsize"] = [15.00, 12.00]
    fig, ax = plt.subplots(4, 2, tight_layout=True)


# ______________________________HISTOGRAMY______________________________#
    # bins=[xx] oznacza zakresy pomiędzy słupkami wykresu
    ax[0][0].hist(Dlug_dzial_kiel, bins=[4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0], edgecolor="black")
    ax[0][0].set_title("Długość działki kielicha")
    ax[0][0].set_xlabel("Długość (cm)")
    ax[0][0].set_ylabel("Liczebność")

    ax[1][0].hist(Szer_dzial_kiel, bins=[2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5], edgecolor="black")
    ax[1][0].set_title("Szerokość działki kielicha")
    ax[1][0].set_xlabel("Szerokość (cm)")
    ax[1][0].set_ylabel("Liczebność")

    ax[2][0].hist(Dlug_plat, bins=[1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0], edgecolor="black")
    ax[2][0].set_title("Długość płatka")
    ax[2][0].set_xlabel("Długość (cm)")
    ax[2][0].set_ylabel("Liczebność")

    ax[3][0].hist(Szer_plat, bins=[0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5], edgecolor="black")
    ax[3][0].set_title("Szerokośc płatka")
    ax[3][0].set_xlabel("Szerokość (cm)")
    ax[3][0].set_ylabel("Liczebność")

# ______________________________WYKRESY_PUDEŁKOWE______________________________#

    # nazwy posczegolnych gatunkow
    g1 = 'setosa'
    g2 = 'versicolor'
    g3 = 'virginica'

    # deklaruje tablice zawierające informacje o poszczegolnych cechach dla danych gatunkow
    Dlug_dzial_kiel_g1 = [None]*50
    Dlug_dzial_kiel_g2 = [None]*50
    Dlug_dzial_kiel_g3 = [None]*50

    Szer_dzial_kiel_g1 = [None]*50
    Szer_dzial_kiel_g2 = [None]*50
    Szer_dzial_kiel_g3 = [None]*50

    Dlug_plat_g1 = [None]*50
    Dlug_plat_g2 = [None]*50
    Dlug_plat_g3 = [None]*50

    Szer_plat_g1 = [None]*50
    Szer_plat_g2 = [None]*50
    Szer_plat_g3 = [None]*50

    # wypelniam je wymaganymi danymi
    for i in range(50):
        Dlug_dzial_kiel_g1[i] = tabela_dlugosci_dzialki_kielicha[i]
        Szer_dzial_kiel_g1[i] = tabela_szerokosci_dzialki_kielicha[i]
        Dlug_plat_g1[i] = tabela_dlugosci_platka[i]
        Szer_plat_g1[i] = tabela_szerokosci_platka[i]

    for i in range(50,100):
        Dlug_dzial_kiel_g2[i-50] = tabela_dlugosci_dzialki_kielicha[i]
        Szer_dzial_kiel_g2[i-50] = tabela_szerokosci_dzialki_kielicha[i]
        Dlug_plat_g2[i-50] = tabela_dlugosci_platka[i]
        Szer_plat_g2[i-50] = tabela_szerokosci_platka[i]

    for i in range(100, 150):
        Dlug_dzial_kiel_g3[i - 100] = tabela_dlugosci_dzialki_kielicha[i]
        Szer_dzial_kiel_g3[i - 100] = tabela_szerokosci_dzialki_kielicha[i]
        Dlug_plat_g3[i - 100] = tabela_dlugosci_platka[i]
        Szer_plat_g3[i - 100] = tabela_szerokosci_platka[i]

    # struktura "dictionary" dostępna w Pythonie pozwala na zadeklarowanie
    # klucza i przypisania do niego danych
    # w tym przypadku pozwala to na wytworzenie trzech osobnych wykresów pudełkowych
    # odpowiadających gatunkom irysów

    Slownik_dlug_dzial_kiel = {g1: Dlug_dzial_kiel_g1, g2: Dlug_dzial_kiel_g2, g3: Dlug_dzial_kiel_g3}
    Slownik_szer_dzial_kiel = {g1: Szer_dzial_kiel_g1, g2: Szer_dzial_kiel_g2, g3: Szer_dzial_kiel_g3}
    Slownik_dlug_plat = {g1: Dlug_plat_g1, g2: Dlug_plat_g2, g3: Dlug_plat_g3}
    Slownik_szer_plat = {g1: Szer_plat_g1, g2: Szer_plat_g2, g3: Szer_plat_g3}

    # tworzę wykresy pudełkowe
    ax[0][1].boxplot(Slownik_dlug_dzial_kiel.values())
    ax[0][1].set_xticklabels(Slownik_dlug_dzial_kiel.keys())
    ax[0][1].set_xlabel("Gatunek")
    ax[0][1].set_ylabel("Długość(cm)")

    ax[1][1].boxplot(Slownik_szer_dzial_kiel.values())
    ax[1][1].set_xticklabels(Slownik_szer_dzial_kiel.keys())
    ax[1][1].set_xlabel("Gatunek")
    ax[1][1].set_ylabel("Szerokość(cm)")

    ax[2][1].boxplot(Slownik_dlug_plat.values())
    ax[2][1].set_xticklabels(Slownik_dlug_plat.keys())
    ax[2][1].set_xlabel("Gatunek")
    ax[2][1].set_ylabel("Długość(cm)")

    ax[3][1].boxplot(Slownik_szer_plat.values())
    ax[3][1].set_xticklabels(Slownik_szer_plat.keys())
    ax[3][1].set_xlabel("Gatunek")
    ax[3][1].set_ylabel("Szerokość(cm)")

    # zapis wygenerowanych wykresów do pliku pdf
    plt.savefig("Wykresy.pdf")

