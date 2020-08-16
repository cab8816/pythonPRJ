from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib import auth
from Myapp.models import Biao4


def beyindex(request):
    return render(request, "beybase.html")


@login_required(login_url='/myapp/signin/')
def beybiao4(request):
    mlstbiao4 = Biao4.objects.all()

    data1 = split_page(mlstbiao4, request, 10)
    return render(request, "bey-biao4.html", data1)


def split_page(object_list, request, per_page=8):
    paginator = Paginator(object_list, per_page)
    # 取出当前需要展示的页码, 默认为1
    page_num = request.GET.get('page', default='1')
    # 根据页码从分页器中取出对应页的数据
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger as e:
        # 不是整数返回第一页数据
        # page = paginator.page('1')
        page = paginator.page('1')
        page_num = 1
    except EmptyPage as e:
        # 当参数页码大于或小于页码范围时,会触发该异常
        print('EmptyPage:{}'.format(e))
        if int(page_num) > paginator.num_pages:
            # 大于 获取最后一页数据返回
            page = paginator.page(paginator.num_pages)
        else:
            # 小于 获取第一页
            page = paginator.page(1)

    # 这部分是为了再有大量数据时，仍然保证所显示的页码数量不超过10，
    page_num = int(page_num)
    if page_num < 6:
        if paginator.num_pages <= 10:
            dis_range = range(1, paginator.num_pages + 1)
        else:
            dis_range = range(1, 11)
    elif (page_num >= 6) and (page_num <= paginator.num_pages - 5):
        dis_range = range(page_num - 5, page_num + 5)
    else:
        dis_range = range(paginator.num_pages - 9, paginator.num_pages + 1)

    data = {'page': page, 'paginator': paginator, 'dis_range': dis_range}
    return data


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    user_obj = auth.authenticate(username=username, password=password)
    if not user_obj:
        return redirect("/myapp/signin/")
    else:
        auth.login(request, user_obj)
        path = request.GET.get("next") or "/myapp/beyindex/"
        rep = redirect(path)
        rep.set_cookie("is_login", True)
        return rep


def logout(request):
    ppp = auth.logout(request)
    return redirect("/myapp/signin/")





def register(request):
    if request.method == "GET":
        captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})
        return render(request, "register.html", {'captcha': captcha})
    else:
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2:
            User.objects.create(username=username, password=password1)
            return redirect("/myapp/signin/")
        else:
            return redirect("/myapp/register/")


def checkuser(request):
    existuser = False

    return existuser
