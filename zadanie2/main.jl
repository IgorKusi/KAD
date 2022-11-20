using CSV
using DataFrames

include("functions.jl")


col_names = ["DDK", "SDK", "DP", "SP", "Gatunek"]
df = CSV.read("dane.csv", header = col_names, DataFrame)    #loading data from .csv file to DataFrame structure 



print(df);
