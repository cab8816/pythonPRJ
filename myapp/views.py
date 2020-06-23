from django.shortcuts import render

# Create your views here.
#
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse(u"欢迎你谢振乾1")
    context={}
    context['hello']='hello ddd  dddddd777 hello tiskk 谢岸马'
    return render(request,'test.html',context)