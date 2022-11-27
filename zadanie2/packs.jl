ENV["PYTHON"]=""
import Pkg;
Pkg.add(["CSV", "DataFrames", "PyCall", "PyPlot"])

using CSV
using DataFrames
using PyCall
using PyPlot