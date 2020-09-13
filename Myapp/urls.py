
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
    path('add_Bpsdwxx/', beyindex.add_Bpsdwxx),
    path('add_Pingshenxxb/', beyindex.add_Pingshenxxb),
    path('add_Xcpshcb/', beyindex.add_Xcpshcb),
    path('register/', beyindex.register),
    path('logout/', beyindex.logout),
    path('ajax_checkuser/', beyindex.ajax_checkuser),
    path('refresh_captcha/', beyindex.refresh_captcha),    # 刷新验证码，ajax




]