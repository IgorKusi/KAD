#minimum tablicy 
function mini(arr::Vector{<:Real})
    var = arr[1] #Julia indeksuje tablice od 1 nie od 0
    for i in range(1, lastindex(arr))
        if arr[i]< var
            var = arr[i] 
        end
    end
    return var
end

#maksimum tablicy 
function maxi(arr::Vector{<:Real})
    var = arr[1] #Julia indeksuje tablice od 1 nie od 0
    for i in range(1,lastindex(arr))
        if arr[i]> var
            var = arr[i] 
        end
    end
    return var
end

#średnia arytmetyczna 
function avg(arr::Vector{<:Real}) 
    summ = 0
    for i in range(1,lastindex(arr))
        summ = summ + arr[i]
    end
    return summ/lastindex(arr)
end

#kowariancja pomiedzy X a Y 
function cov(arrX::Vector{<:Real}, arrY::Vector{<:Real})
    pr::Vector{Real} = []
    for i in range(1, lastindex(arrX))
        push!(pr, arrX[i] * arrY[i])
    end
    avgX = avg(arrX)
    avgY = avg(arrY)
    avgPr = avg(pr)

    avgXY = avgX * avgY 
    return avgPr - avgXY

end

#odchylenie standardowe z próby
function sd(arr::Vector{<:Real}) 
    av = avg(arr)
    summ = 0
    for i in range(1,lastindex(arr))
        summ = summ + ((arr[i] - av)*(arr[i] - av))
    end
    return sqrt(summ/(lastindex(arr)-1))
end

function Pearson(arrX::Vector{<:Real}, arrY::Vector{<:Real})
   return (cov(arrX, arrY))/(sd(arrX)*sd(arrY))
end

#funkcja zwracajaca wspolczynnik kierunkowy a regresji liniowej 
function regLine_A(arrX::Vector{<:Real}, arrY::Vector{<:Real})
    

    #krok 1 - obliczam roznice miedzy x, a avg(x); tak samo dla y  
   
    arrDeltaX::Vector = []     #tablica różnic pomiedzy kolejnymi X a średnia arytmetyczną ze wszystkich X
    arrDeltaY::Vector = []     # ^ , ale Y  
    avgX = avg(arrX)                     #zapisuje te avg w zmiennych zeby nie wywoływać 300 razy funkcji w pętli ponizej
    avgY = avg(arrY)
    for i in range(1,lastindex(arrX))
        push!(arrDeltaX, arrX[i] - avgX) 
        push!(arrDeltaY, arrY[i] - avgY)
    end

    #krok 2 - mnoze te różnice 

    arrDeltasMultiplied::Vector  = []
    for i in range(1,lastindex(arrX))
        push!(arrDeltasMultiplied, *(arrDeltaX[i], arrDeltaY[i]))
    end

    #krok 3 - tablica roznic x i avg(x) podniesiona do kwadratu 

    arrDeltaXsquare::Vector = []
    for i in range(1,lastindex(arrX))
        push!(arrDeltaXsquare, *(arrDeltaX[i], arrDeltaX[i]) )
    end

    #krok 4 -sumuje wszystkie wartosci w tablicy z kroku 2, i wszystkie wartosci z kroku 3 (nie ze sobą, tylko osobno dwie sumy poszczegolnych tablic)

    sumArrDeltasMultiplied = 0
    sumArrDeltaXsquare = 0

    for i in range(1,lastindex(arrX))
        sumArrDeltasMultiplied = sumArrDeltasMultiplied + arrDeltasMultiplied[i]
        sumArrDeltaXsquare = sumArrDeltaXsquare + arrDeltaXsquare[i]
    end

    #krok 5 - obliczam a 
    a = sumArrDeltasMultiplied / sumArrDeltaXsquare
    return a;
    
end

function regLine_B(arrX::Vector{<:Real}, arrY::Vector{<:Real}, regA = regLine_A(arrX, arrY))
    avgX = avg(arrX)
    avgY = avg(arrY)
    b = avgY - (regA * avgX)
    
    return b
end


function regLine_Wzor(arrX::Vector{<:Real}, arrY::Vector{<:Real})


    a = regLine_A(arrX, arrY)
    b = regLine_B(arrX, arrY)

    wzor = string("y = ", round(a; digits = 1), "x")
    if b > 0
        wzor = string(wzor,  " + ", round(b; digits=1))
        return wzor
    end
    
    if b == 0 
        return wzor
    end

    if b < 0 
        wzor = string(wzor, " - ", abs(round(b; digits=1)))
        return wzor
    end
end

function regLine_Wzor(a::Real, b::Real)
    return """y = $(round(a, digits = 1))x $(b > 0 ? "+" : (b == 0 ? "" : "-")) $(abs(round(b, digits = 1)))""";
end