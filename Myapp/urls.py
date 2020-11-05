
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
    path('add_Bpsdwxx/', beyindex.add_Bpsdwxx),
    path('add_Pingshenxxb/', beyindex.add_Pingshenxxb),
    path('edit_Pingshenxxb/', beyindex.edit_Pingshenxxb),
    path('del_Pingshenxxb/', beyindex.del_Pingshenxxb),
    path('lst_Pingshenxxb/', beyindex.lst_Pingshenxxb),
    path('edit_bufuhexiang/', beyindex.edit_bufuhexiang),
    path('add_bufuhexiang/', beyindex.add_bufuhexiang),
    path('add_Xcpshcb/', beyindex.add_Xcpshcb),
    path('register/', beyindex.register),
    path('logout/', beyindex.logout),
    path('ajax_checkuser/', beyindex.ajax_checkuser),
    path('refresh_captcha/', beyindex.refresh_captcha),    # 刷新验证码，ajax




]