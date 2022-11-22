#minimum tablicy 
function mini(arr::Vector)
    var = arr[1] #Julia indeksuje tablice od 1 nie od 0
    for i in range(1, lastindex(arr))
        if arr[i]< var
            var = arr[i] 
        end
    end
    return var
end

#maksimum tablicy 
function maxi(arr::Vector)
    var = arr[1] #Julia indeksuje tablice od 1 nie od 0
    for i in range(1,lastindex(arr))
        if arr[i]> var
            var = arr[i] 
        end
    end
    return var
end

#średnia arytmetyczna 
function avg(arr::Vector) 
    summ = 0
    for i in range(1,lastindex(arr))
        summ = summ + arr[i]
    end
    return summ/lastindex(arr)
end

#kowariancja pomiedzy X a Y 
function cov(arrX::Vector, arrY::Vector)
    pr::Vector = []
    for i in range(1, lastindex(arrX))
        push!(pr, arrX[i] * arrY[i])
    end
    avgX = avg(arrX)
    avgY = avg(arrY)
    avgPr = avg(pr)

    avgXY = avgX * avgY 
    return avgPr - avgXY

end

#odchylenie standardowe z populacji
function sd(arr::Vector) 
    av = avg(arr)
    summ = 0
    for i in range(1,lastindex(arr))
        summ = summ + ((arr[i] - av)*(arr[i] - av))
    end
    return sqrt(summ/lastindex(arr))
end

function Pearson(arrX::Vector, arrY::Vector)
   return (cov(arrX, arrY))/(sd(arrX)*sd(arrY))
end

#funkcja zwracajaca wspolczynnik kierunkowy a regresji liniowej 
function regLine_A(arrX::Vector, arrY::Vector)
    #https://www.statystyczny.pl/regresja-liniowa/

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

function regLine_B(arrX::Vector, arrY::Vector)
    avgX = avg(arrX)
    avgY = avg(arrY)
    a = regLine_A(arrX, arrY)
    b = avgY - (a * avgX)
    
    return b
end

function regLine_Wzor(arrX::Vector, arrY::Vector)
    #poki co zostawiam to tak jak jest - w 3 osobnych funkcjach - bo nie wiem jak bedziemy korzystac z tych wartosci 
    #i nie znam sie na Julce (kiedys z jedna krecilem i mnie olała)
    #(jestem zemstą)
    #(sth in the way, mmmmmmm mmmmm )

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
