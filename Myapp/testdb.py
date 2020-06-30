from django.http import HttpResponse

from Myapp.models import Students


def testdbadd(request):
    student = Students(name='谢振乾')
    student.save()
    return HttpResponse("<p> 数据添加成功！</p>")


def testdblst(request):
    response1 = ""
    list = Students.objects.all()
    for var in list:
        response1 += var.name + " "
    return HttpResponse("<p>" + response1 + "</p>")


def testdbupd(request):
    stu = Students.objects.get(id=2)
    stu.name = '谢岸马'
    stu.save()
    stu.objects.filter(id=3).update(name='谢多多')
    return HttpResponse("<p>成功修改</p>")
