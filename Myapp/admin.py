from django.contrib import admin
from Myapp.models import Biao4
from .utils import import_user

# Register your models here.
# python manage.py createsuperuser
# admin cab88 xzq254613
# cab777  bbbb4321

class Biao4Admin(admin.ModelAdmin):
    list_display = ('lyname','lb','duixiang','csmc')

admin.site.register(Biao4,Biao4Admin)


# class KNImportFileAdmin(admin.ModelAdmin):
#     list_display = ('file', 'name',)
#     list_filter = ['name', ]
#
#     def save_model(self, request, obj, form, change):
#         re = super(YDImportFileAdmin, self).save_model(request, obj, form, change)
#         import_user(self, request, obj, change)
#         return re