using CSV
using DataFrames
using PyPlot

include("functions.jl")
include("plotting.jl")

#TODO - juz tylko wykresy


#_______________________________________________________WCZYTYWANIE Z PLIKU_______________________________________________________#

col_names = ["DDK", "SDK", "DP", "SP", "Gatunek"]                                       #array stringow z labelami kolumn -> pewnie niepotrzebne, ale bardziej czytelne wczytywanie kolumn w dalszych krokach

df = CSV.read("dane.csv", header = col_names, DataFrame)                                #zasysam dane z csv do DataFrame, wszystko jak leci 


#archaizm - nie jest to już wcale potrzebne, zostawiłem zeby było widac ze w razie co to sie da
# |
# V
#dfDDK = CSV.read("dane.csv", header = col_names, select = [:DDK], DataFrame)            #zasysam tylko kolumne z labelem "DDK"


DDK = df.DDK                     #konwertuje kolumne DataFrame na vector floatow (yes, indeed it is that simple)
SDK = df.SDK                     #vector to własciwie alias dla typu Array{T, 1} gdzie T to typ zmiennych
DP = df.DP                       #w ten sam spobób jak Matrix to Array{T, 2}
SP = df.SP
Gatunek = df.Gatunek

#______________________________jakies printy do testowania___________________________#

# print(typeof(DDK), "-> DDK","\n", DDK, "\n", "\n",
#         typeof(SDK),"-> SDK","\n", SDK,"\n","\n",    
#         typeof(DP),"-> DP","\n", DP,"\n","\n",
#         typeof(SP),"-> SP","\n", SP,"\n","\n",
#         typeof(Gatunek),"-> Gatunek","\n",Gatunek )

# print("\n","\n","\n","Długość działki kielicha: ", "\n")
# print("min: ", mini(DDK), "\n")
# print("max: ", maxi(DDK), "\n")
# print("avg: ", avg(DDK), "\n")
# print("sd: ", sd(DDK), "\n")

# print("\n","Szerokość płatka: ", "\n")
# print("min: ", mini(SP), "\n")
# print("max: ", maxi(SP), "\n")
# print("avg: ", avg(SP), "\n")
# print("sd: ", sd(SP), "\n")

# print("\n","Pearson DDK, SDK: ",round(Pearson(DDK,SDK); digits = 2 ), "\n")

# print("\n", "Regline DDK SDK", "\n")
# print("a: ", regLine_A(DDK,SDK), "\n" ,"b: ", regLine_B(DDK,SDK), "\n", "wzor: ",regLine_Wzor(DDK, SDK), "\n")


makePlots(DDK, SDK, DP, SP);
