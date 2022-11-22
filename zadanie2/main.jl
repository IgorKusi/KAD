using CSV
using DataFrames

include("functions.jl")

#TODO osobny plik na wykresy, ustalic z jakiej biblioteki bedizemy korzstac do tego 
#TODO sprawdzic czy funckje statystyczne dzialaja jak powinny - porownac z tym co na stronie przedmiotu, ewentualnie zrobic w excelu 


#_______________________________________________________WCZYTYWANIE Z PLIKU_______________________________________________________#

col_names = ["DDK", "SDK", "DP", "SP", "Gatunek"]                                       #array stringow z labelami kolumn -> pewnie niepotrzebne, ale bardziej czytelne wczytywanie kolumn w dalszych krokach

df = CSV.read("dane.csv", header = col_names, DataFrame)                                #zasysam dane z csv do DataFrame, wszystko jak leci 


#archaizm - nie jest to już wcale potrzebne, zostawiłem zeby było widac ze w razie co to sie da
# |
# V
#dfDDK = CSV.read("dane.csv", header = col_names, select = [:DDK], DataFrame)            #zasysam tylko kolumne z labelem "DDK"
#dfSDK = CSV.read("dane.csv", header = col_names, select = [:SDK], DataFrame)            
#dfDP = CSV.read("dane.csv", header = col_names, select = [:DP], DataFrame)
#dfSP = CSV.read("dane.csv", header = col_names, select = [:SP], DataFrame)
#dfGatunek = CSV.read("dane.csv", header = col_names, select = [:Gatunek], DataFrame)

DDK = df.DDK                                                            #konwertuje kolumne DataFrame na vector floatow (yes, indeed it is that simple)
SDK = df.SDK                                                            #vector to własciwie alias dla typu Array{T, 1} gdzie T to typ zmiennych
DP = df.DP                                                              #w ten sam spobób jak Matrix to Array{T, 2}
SP = df.SP
Gatunek = df.Gatunek


#print(typeof(DDK),"\n", DDK, "\n","\n",typeof(SDK),"\n",SDK,"\n","\n",typeof(DP),"\n",DP,"\n","\n",typeof(SP),"\n",SP,"\n","\n",typeof(Gatunek),"\n",Gatunek )

print(Pearson(SDK, DDK))
print("\n", regLine(DDK, SDK))