from django.shortcuts import render


def beyindex(request):
    return render(request, "beybase.html")

def beybiao4(request):
    return render(request,"bey-biao4.html")
