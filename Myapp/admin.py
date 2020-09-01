import datetime

from PIL._imagingmorph import apply
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.template.defaultfilters import register

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

# 按住ALT，用鼠标在需要的位置点击添加光标，然后输入内容即可

# pip freeze > requirements.txt
# cd
# python -m venv scrapy_env
# cd scrapy_env/scripts
# activate
# pip install -r requirements.txt







from Myapp.utils import importpsymd


class UsersFilter(SimpleListFilter):
    title = '用户名'
    parameter_name = 'user'

    def lookups(self, request, model_admin):
        return [(1, '已下线'), (2, '进行中'), (3, '未到测试区间')]

    def queryset(self, request, queryset):
        # this_day = datetime.date.today()
        # pdb.set_trace()
        return queryset.filter(user = 'cab88')
        #
        # if self.value() == '3':
        #     return queryset.filter(test_start_date__gt=this_day)
        # elif self.value() == '1':
        #     return queryset.filter(test_end_date__lt=this_day)
        # elif self.value() == '2':
        #     return queryset.filter(test_end_date__gte=this_day, test_start_date__lte=this_day)


def readed(modeladmin, request, queryset):
    queryset.update(sm='已点')


@admin.register(Biao4)
class Biao4Admin(admin.ModelAdmin):
    list_display = ('id', 'xmxh', 'lb', 'duixiang', 'csmc', 'yjbz', 'xzfw', 'sm', 'dis_pstzh')
    # search_fields = ('duixiang', 'csmc', 'lb')  # 搜索字段
    # fields = ('xmxh', 'lb', 'duixiang', 'csmc',)
    actions = [readed]

    def dis_pstzh(self, obj):
        return obj.psxxb.pstzh

    dis_pstzh.short_description = "评审通知号"


@admin.register(ImportFile)
class ImportFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'dis_pstzh', 'dis_importtype', 'file',)

    def dis_pstzh(self, obj):
        return obj.psxxb.pstzh

    # def dis_psxxb_id(self, obj):
    #     return obj.psxxb.id

    def dis_importtype(self, obj):
        # print(obj.importtype)
        return obj.get_importtype_display()

    dis_importtype.short_description = '读取文件类型'
    # dis_psxxb_id.short_description ="信息编号"
    dis_pstzh.short_description = "评审通知号"

    def save_model(self, request, obj, form, change):
        re = super().save_model(request, obj, form, change)

        importpsymd(self, request, obj, change)
        return re


@register.filter(name='displayname')
def displayname(value, arg):
    return apply(eval('value.get_' + arg + '_display'), ())


@admin.register(Biao5)
class Biao5admin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'name', 'ziwuzicheng', 'sqqzly', 'beizu', 'dis_pstzh')

    def dis_pstzh(self, obj):
        return obj.psxxb.pstzh

    dis_pstzh.short_description = "评审通知号"

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
    list_display = ('id', 'name', 'gender', 'danwei', 'psybh',)


@admin.register(Pingshenxxb)
class PingshenxxbAdmin(admin.ModelAdmin):
    list_display = ('id', 'dis_user', 'pstzh', 'jcjgmc')
    list_filter = ('pstzh',)

    def dis_user(self, obj):
        return obj.user

    dis_user.short_description = "用户名"


@admin.register(Biao72)
class Biao72Admin(admin.ModelAdmin):
    list_display = ('xuhao', 'xmmc', 'yjbz', 'xmxh', 'csmc', 'dis_pstzh')

    def dis_pstzh(self, obj):
        return obj.psxxb.pstzh

    dis_pstzh.short_description = "评审通知号"


@admin.register(Pszcy)
class PszcyAdmin(admin.ModelAdmin):
    list_display = ('psyzc', 'psname', 'ziwuzicheng', 'gzdw', 'lxfs', 'dis_pstzh')

    def dis_pstzh(self, obj):
        return obj.psxxbs.first().pstzh

    dis_pstzh.short_description = "评审通知号"


@admin.register(Bpsdwxx)
class BpsdwxxAdmin(admin.ModelAdmin):
    list_display = ('jyjcjgmc', 'zcdz', 'jydz', 'yzbm')

    # def dis_pstzh(self, obj):
    #     return obj.psxxbs.first().pstzh
    # dis_pstzh.short_description = "被评审单位信息"
