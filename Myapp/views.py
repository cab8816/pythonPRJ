# Create your views here.
#
from django.shortcuts import render


def index(request):
    # return HttpResponse(u"欢迎你谢振乾1")
    # auth.logout(request)
    context = {}
    context['hello'] = 'hello ddd 2020/06/24 10:05 dddddd777 hello tiskk 谢岸马'
    context['msg'] = 'msgggggggg'

    return render(request, 'index.html', context)


def zzindex(request):
    return render(request, 'base.html')
