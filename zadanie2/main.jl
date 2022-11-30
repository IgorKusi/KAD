using CSV
using DataFrames
using PyPlot

include("functions.jl")
include("plotting.jl")


col_names = ["DDK", "SDK", "DP", "SP", "Gatunek"]                                       #array stringow z labelami kolumn -> pewnie niepotrzebne, ale bardziej czytelne wczytywanie kolumn w dalszych krokach

df = CSV.read("dane.csv", header = col_names, DataFrame)                                

DDK = df.DDK                     #konwertuje kolumne DataFrame na vector floatow 
SDK = df.SDK                     #vector to własciwie alias dla typu Array{T, 1} gdzie T to typ zmiennych
DP = df.DP                       #w ten sam spobób jak Matrix to Array{T, 2}
SP = df.SP
Gatunek = df.Gatunek


makePlots(DDK, SDK, DP, SP);
