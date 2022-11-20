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