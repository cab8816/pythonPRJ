from django.db import models

#
# # Assume you are activating Python 3 venv
# $ brew install mysql-client
# $ echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.bash_profile
# $ export PATH="/usr/local/opt/mysql-client/bin:$PATH"
# $ pip install mysqlclient

# $ python3 manage.py migrate   # 创建表结构
#
# $ python3 manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
# $ python3 manage.py migrate TestModel   # 创建表结构

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=20)


class Biao4(models.Model):
    id = models.AutoField(primary_key=True)
    psxh = models.CharField(max_length=20)
    lyxh = models.CharField(max_length=20)
    lyname = models.CharField(max_length=100)
    lbxh = models.CharField(max_length=20)
    lb = models.CharField(max_length=100)
    dxxh = models.CharField(max_length=20)
    duixiang = models.CharField(max_length=100)
    xmxh = models.CharField(max_length=20)
    xmmc = models.CharField(max_length=100)
    csmc = models.CharField(max_length=100)
    yjbz = models.CharField(max_length=300)
    xzfw = models.CharField(max_length=100)
    sm = models.CharField(max_length=200)

    def __str__(self):
        return self.csmc
