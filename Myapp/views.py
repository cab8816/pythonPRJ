from django.shortcuts import render

# Create your views here.
#
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse(u"欢迎你谢振乾1")
    context = {}
    context['hello'] = 'hello ddd 2020/06/24 10:05 dddddd777 hello tiskk 谢岸马'
    return render(request, 'test.html', context)
