import datetime

from django.contrib import admin

from Myapp.models import *

# from .utils import import_user

# Register your models here.
# python manage.py createsuperuser
# admin cab88 xzq254613
# cab777  bbbb4321

# pip install -i https://pypi.douban.com/simple

# C:\Users\Administrator\下新建 pip  文件夹，然后创建pip.ini文件，拷贝下面代码进去，保存。
#
# [global]
# index-url = https://pypi.tuna.tsinghua.edu.cn/simple
from Myapp.utils import importpsymd


def readed(modeladmin, request, queryset):
    queryset.update(sm='已点')


@admin.register(Biao4)
class Biao4Admin(admin.ModelAdmin):
    list_display = ('id', 'xmxh', 'lb', 'duixiang', 'csmc', 'yjbz', 'xzfw', 'sm','psxxb')
    # search_fields = ('duixiang', 'csmc', 'lb')  # 搜索字段
    # fields = ('xmxh', 'lb', 'duixiang', 'csmc',)
    actions = [readed]


@admin.register(ImportFile)
class ImportFileAdmin(admin.ModelAdmin):
    list_display = ('importtype', 'file',)

    def save_model(self, request, obj, form, change):
        re = super().save_model(request, obj, form, change)

        importpsymd(self, request, obj, change)
        return re



@admin.register(Biao5)
class Biao5admin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'name', 'ziwuzicheng', 'sqqzly', 'beizu','psxxb')

    # # list_per_page设置每页显示多少条记录，默认是100条
    # list_per_page = 50
    # # ordering设置默认排序字段，负号表示降序排序
    # ordering = ('id',)
    # # list_editable 设置默认可编辑字段
    # list_editable = ['name', 'ziwuzicheng']
    #
    # # fk_fields 设置显示外键字段
    # fk_fields = ('name',)
    #
    # # 设置哪些字段可以点击进入编辑界面
    # # list_display_links = ('id', 'name')
    # # 筛选器
    # list_filter = ('name', 'ziwuzicheng',)  # 过滤器
    # search_fields = ('beizu',)  # 搜索字段
    # # date_hierarchy = 'ziwuzicheng'  # 详细时间分层筛选　

    # python - m django - -version


@admin.register(PsyuanDetail)
class PsyuanDetailAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'gender', 'danwei', 'psybh',)

@admin.register(Pingshenxxb)
class PingshenxxbAdmin(admin.ModelAdmin):
    list_display = ('id','pstzh',)



@admin.register(Biao72)
class Biao72Admin(admin.ModelAdmin):
    list_display = ('xuhao', 'xmmc','yjbz','xmxh','csmc','psxxb')

@admin.register(Pszcy)
class PszcyAdmin(admin.ModelAdmin):
    list_display = ('psyzc', 'psname','ziwuzicheng','gzdw','lxfs',)