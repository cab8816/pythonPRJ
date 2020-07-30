from django.contrib import admin
from Myapp.models import Biao4

# Register your models here.
# python manage.py createsuperuser
# admin cab88 xzq254613

class Biao4Admin(admin.ModelAdmin):
    list_display = ('lyname','lb','duixiang','csmc')

admin.site.register(Biao4,Biao4Admin)
