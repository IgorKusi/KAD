import Func as f
import pandas as pd
import matplotlib.pyplot as plt

# fig, ax = plt.subplots(4, 2, tight_layout=True)

def histogram(dane, numer_wiersza=0):
    plt.figure()
    plt.rcParams["figure.figsize"] = [6.00, 5.00]
    ax[numer_wiersza][0].hist(dane, bins=8)

    # plt.show()

