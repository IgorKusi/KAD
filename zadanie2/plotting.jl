using PyPlot

labels = Dict([
    (:SDK, "Szerokość działki kielicha (cm)"),
    (:DDK, "Długość działki kielicha (cm)"),
    (:DP, "Długość płatka (cm)"),
    (:SP, "Szerokość płatka (cm)")
])

function makePlots(DDK::Vector{<:Real}, SDK::Vector{<:Real}, DP::Vector{<:Real}, SP::Vector{<:Real})

    PyPlot.rc("figure", figsize=(7, 10));
    fig, ax = PyPlot.subplots(3, 2, tight_layout = true)

    makePlot(ax[1], DDK, SDK, (x = labels[:DDK], y = labels[:SDK]));
    makePlot(ax[2], DDK, SP, (x = labels[:DDK], y = labels[:SP]));
    makePlot(ax[3], SDK, SP, (x = labels[:SDK], y = labels[:SP]));
    makePlot(ax[4], DDK, DP, (x = labels[:DDK], y = labels[:DP]));
    makePlot(ax[5], SDK, DP, (x = labels[:SDK], y = labels[:DP]));
    makePlot(ax[6], DP, SP, (x = labels[:DP], y = labels[:SP]));

    ax[1].set_xlim([4, 8.1]);
    ax[2].set_xlim([4, 8.1]);
    ax[2].set_ylim([0, 3]);
    ax[3].set_xlim([1.9, 4.6]);
    ax[4].set_xlim([4, 8.1]);
    ax[4].set_ylim([0.7, 8]);
    ax[5].set_xlim([1.9, 4.6]);
    ax[6].set_xlim([-0.1, 8.1]);

    PyPlot.savefig("wykresy.pdf")
end

function getPlotTitle(r::Real, a::Real, b::Real)
    return "r = $(round(r, digits = 2)); $(regLine_Wzor(a, b))";
end

function makePlot(axes, arrX::Vector{<:Real}, arrY::Vector{<:Real}, labels::NamedTuple{(:x, :y)})
    r = Pearson(arrX, arrY);
    a = regLine_A(arrX, arrY);
    b = regLine_B(arrX, arrY, a);

    axes.scatter(arrX, arrY);                           #wykres punktowy
    axes.set_title(getPlotTitle(r, a, b));
    axes.set_xlabel(labels.x);
    axes.set_ylabel(labels.y);
    axes.plot(arrX, a.*arrX .+ b, color = "red");       #nałożenie nań wykresu liniowego - regresji liniowej
    axes.set_aspect("auto");
end
