from django.shortcuts import render
from . import nas_modul

# Create your views here.

def kalkulacka(request):
    error_msg = None
    vysledek = None
    floatA = request.POST["a"]
    floatB = request.POST["b"]
    operator = request.POST["operator"]
    if request.method == "POST":
        try:
            float(request.POST["a"])
            float(request.POST["b"])
        except:
            error_msg = "A nebo B není číslo!"
            return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledek=vysledek))

        if (float(request.POST["a"] == 0 and request.POST["operator"]=="/")):
            error_msg = "chyba dělení nulou"
            return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledek=vysledek))
        if(operator)== "+":
            vysledek = nas_modul.soucin(floatA, floatB)
        elif(operator)== "-":
            vysledek = nas_modul.podil(floatA, floatB)
        elif(operator)== "*":
            vysledek = nas_modul.soucin(floatA, floatB)
        elif(operator) == "/":
            vysledek == nas_modul.podil(floatA, floatB)
        else:
            error_msg = "Něco se pokazilo"
            return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledek=vysledek))
    return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledek=vysledek))