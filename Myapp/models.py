from django.db import models


# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=20)


class Biao4(models.Model):
    id = models.AutoField(primary_key=True)
    psxh = models.CharField(max_length=20)
    lyxh = models.CharField(max_length=20)
    lyname = models.CharField(max_length=50)
    lbxh = models.CharField(max_length=20)
    lb = models.CharField(max_length=50)
    dxxh = models.CharField(max_length=20)
    duixiang = models.CharField(max_length=50)
    xmxh = models.CharField(max_length=20)
    xmmc = models.CharField(max_length=50)
    csmc = models.CharField(max_length=50)
    yjbz = models.CharField(max_length=200)
    xzfw = models.CharField(max_length=100)
    sm = models.CharField(max_length=200)
