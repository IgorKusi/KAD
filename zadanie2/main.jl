using CSV
using DataFrames

include("functions.jl")

#TODO wyciagnac z DataFrame pojedyncze kolumny jako Array, ew wczytac je od razu do arraya 
#TODO osobny plik na wykresy, ustalic z jakiej biblioteki bedizemy korzstac do tego 
#TODO sprawdzic czy funckje statystyczne dzialaja jak powinny - porownac z tym co na stronie przedmiotu, ewentualnie zrobic w excelu 

col_names = ["DDK", "SDK", "DP", "SP", "Gatunek"]
df = CSV.read("dane.csv", header = col_names, DataFrame)    #loading data from .csv file to DataFrame structure 


print(df);
