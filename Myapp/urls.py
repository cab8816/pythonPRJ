
from django.urls import path

from Myapp import views, testdb, beyindex

urlpatterns = [
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
    path('signin/', beyindex.signin),
    path('person/', beyindex.person),

    path('Bfhxiang_del/', beyindex.Bfhxiang_del),
    path('Bfhxiang_add/', beyindex.Bfhxiang_add),
    path('Bfhxiang_edit/', beyindex.Bfhxiang_edit),
    path('Bfhxiang_list/', beyindex.Bfhxiang_list),
    path('showhctkxx/', beyindex.showhctkxx),

    path('Bpsdwxx_add/', beyindex.Bpsdwxx_add),

    path('Pingshenxxb_add/', beyindex.Pingshenxxb_add),
    path('Pingshenxxb_edit/', beyindex.Pingshenxxb_edit),
    path('Pingshenxxb_del/', beyindex.Pingshenxxb_del),
    path('Pingshenxxb_list/', beyindex.Pingshenxxb_list),

    path('register/', beyindex.register),
    path('logout/', beyindex.logout),
    path('ajax_checkuser/', beyindex.ajax_checkuser),
    path('refresh_captcha/', beyindex.refresh_captcha),    # 刷新验证码，ajax




]