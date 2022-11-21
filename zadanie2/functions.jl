#minimum tablicy 
function mini(arr::Array{Number})
    var = arr[1] #Julia indeksuje tablice od 1 nie od 0
    for i in arr
        if arr[i]< var
            var = arr[i] 
        end
    end
    return var
end

#maksimum tablicy 
function maxi(arr::Array{Number})
    var = arr[1] #Julia indeksuje tablice od 1 nie od 0
    for i in arr
        if arr[i]> var
            var = arr[i] 
        end
    end
    return var
end

#średnia arytmetyczna 
function avg(arr::Array{Number}) 
    summ = 0
    for i in arr
        summ = summ + i
    summ/length(arr);
    end
end

#kowariancja pomiedzy X a Y 
function cov(arrX::Array{Number}, arrY::Array{Number})
    pr::Array{Number} =[0]
    Ex = avg(arrX)
    Ey = avg(arrY)
    for i in range(length(arrX))
        pr[i] = arrX[i] * arrY[i]
    
    avg(pr) - (Ex * Ey);
    end
end

#odchylenie standardowe z populacji
function sd(arr::Array{Number}) 
    av = avg(arr)
    summ = 0
    for i in arr
        summ = summ + ((arr[i] - av)*(arr[i] - av))
    sqrt(summ/length(arr));
    end
end

function Pearson(arrX::Array{Number}, arrY::Array{Number})
    (cov(arrX, arrY))/(sd(arrX)*sd(arrY))
end

function regLine(arrX::Array{Number}, arrY::Array{Number})
    #https://www.statystyczny.pl/regresja-liniowa/

    #krok 1 - obliczam roznice miedzy x, a avg(x); tak samo dla y  
   
    arrDeltaX::Array{Number} = [0]     #tablica różnic pomiedzy kolejnymi X a średnia arytmetyczną ze wszystkich X
    arrDeltaY::Array{Number} = [0]     # ^ , ale Y  
    avgX = avg(arrX)                     #zapisuje te avg w zmiennych zeby nie wywoływać 300 razy funkcji w pętli ponizej
    avgY = avg(arrY)
    for i in lastindex(arrX)
        arrDeltaX[i] = arrX[i] - avgX 
        arrDeltaY[i] = arrY[i] - avgY
    end

    #krok 2 - mnoze te różnice 

    arrDeltasMultiplied::Array{Number}  = [0]
    for i in lastindex(arrX)
        arrDeltasMultiplied[i] = *(arrDeltaX[i], arrDeltaY[i]) #ale fancy mnozenie hehe lols 
    end

    #krok 3 - tablica roznic x i avg(x) podniesiona do kwadratu 

    arrDeltaXsquare::Array{Number} = [0]
    for i in lastindex(arrX)
        arrDeltaXsquare[i] = *(arrDeltaX[i], arrDeltaX[i])
    end

    #krok 4 -sumuje wszystkie wartosci w tablicy z kroku 2, i wszystkie wartosci z kroku 3 (nie ze sobą, tylko osobno dwie sumy poszczegolnych tablic)

    sumArrDeltasMultiplied = 0
    sumArrDeltaXsquare = 0

    for i in lastindex(arrX)
        sumArrDeltasMultiplied = sumArrDeltasMultiplied + arrDeltasMultiplied[i]
        sumArrDeltaXsquare = sumArrDeltaXsquare + arrDeltaXsquare[i]
    end

    #krok 5 - obliczam a oraz b  
    a = sumArrDeltasMultiplied / sumArrDeltaXsquare

    b = avgY - (a * avgX)

    #w tej formie, cala ta funckja zwroci b jako wynik ostatniego dzialania
    #poki co zostawiam to tak jak jest, bo nie wiem jak bedziemy korzystac z tych wartosci 
    #i nie znam sie na Julce (kiedys z jedna krecilem i mnie olała)
    #(jestem zemstą)
    
end