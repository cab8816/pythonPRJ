from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth

from Myapp.My_forms import PsdwxxForm, PingshenxxbForm, XcpshcbForm
from Myapp.models import Biao4, Bpsdwxx, Pingshenxxb, Xcpshcb71, Xcpshcb
from django.urls import reverse


def beyindex(request):
    return render(request, "bey-base.html")


@login_required(login_url='/myapp/signin/')
def beybiao4(request):
    mlstbiao4 = Biao4.objects.all()

    data1 = split_page(mlstbiao4, request, 10)
    return render(request, "bey-biao4.html", data1)


@login_required(login_url='/myapp/signin/')
def beybiao71(request):
    mlstbiao4 = Biao4.objects.all()

    data1 = split_page(mlstbiao4, request, 10)
    return render(request, "bey-biao71.html", data1)


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
        rep.set_cookie("user1", username)
        request.session['is_login'] = True
        request.session['user1'] = username
        return rep


def logout(request):
    ppp = auth.logout(request)
    return redirect("/myapp/signin/")


# 创建验证码
def captcha():
    # 验证码，第一次请求
    hashkey = CaptchaStore.generate_key()
    image_url = captcha_image_url(hashkey)
    captcha = {'hashkey': hashkey, 'image_url': image_url}
    return captcha


# 验证验证码
def jarge_captcha(captchaStr, captchaHashkey):
    if captchaStr and captchaHashkey:
        try:
            # 获取根据hashkey获取数据库中的response值
            get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey)
            # 如果验证码匹配
            if get_captcha.response == captchaStr.lower():
                return True
            else:
                return False
        except:
            return False
    else:
        return False


# 刷新验证码
import json


def refresh_captcha(request):
    return HttpResponse(json.dumps(captcha()), content_type='application/json')


def person(request):
    return render(request, "demo.html")


def register(request):
    if request.method == "GET":

        return render(request, "register.html")
    else:
        captchaHashkey = request.POST.get("hashkey")
        captchaStr = request.POST.get("captcha")
        bashkey_isok = jarge_captcha(captchaStr, captchaHashkey)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2 and bashkey_isok:
            User.objects.create_user(username=username, password=password1)
            return redirect("/myapp/signin/")
        else:
            return redirect("/myapp/register/")


# 检测用户名是否已被注册
def ajax_checkuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        try:
            getusername = User.objects.get(username=username)
            if getusername.username == username:
                return HttpResponse("1")
        except:
            return HttpResponse("0")
    return redirect("/myapp/register/")


# 密码 组成  ^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,16}$

def add_Bpsdwxx(request):
    if request.method == "GET":
        form = PsdwxxForm()
        return render(request, "bpsdwxx.html", {"form": form})
    else:
        form = PsdwxxForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Bpsdwxx.objects.create(**data)
            form = PsdwxxForm()
            return render(request, "bpsdwxx.html", {"form": form})
        else:
            clean_errors = form.errors.get("__all__")
        return render(request, "bpsdwxx.html", {"form": form, "clean_errors": clean_errors})


def add_Pingshenxxb(request):
    if request.method == "GET":
        form = PingshenxxbForm()
        return render(request, "pingshengxxbForm.html", {"form": form})
    else:
        form = PingshenxxbForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Pingshenxxb.objects.create(**data)
            form = PingshenxxbForm()
            return render(request, "pingshengxxbForm.html", {"form": form})
        else:
            clean_errors = form.errors.get("__all__")
        return render(request, "pingshengxxbForm.html", {"form": form, "clean_errors": clean_errors})


def add_Xcpshcb(request):
    mlstbiao = Xcpshcb.objects.all()
    data1 = split_page(mlstbiao, request, 20)
    return render(request, "Xcpshcb71.html", data1)
