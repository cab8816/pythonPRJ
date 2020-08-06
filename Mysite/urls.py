"""Mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Myapp import views, testdb, beyindex

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('zzindex/', views.zzindex),
    path('testdbadd/', testdb.testdbadd),
    path('testdblst/', testdb.testdblst),
    path('testdbupd/', testdb.testdbupd),
    path('testdoc/', testdb.testdoc),
    path('readword/', testdb.readword),
    path('lstbiao4/', testdb.lstbiao4),
    path('genbiao4/', testdb.genbiao4),
    path('changeword/', testdb.changeword),
    path('uploadfile/', testdb.uploadfile),
    path('downloadfile/', testdb.downloadfile),
    path('beyindex/', beyindex.beyindex),
    path('beybiao4/', beyindex.beybiao4),


]
