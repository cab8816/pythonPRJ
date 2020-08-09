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
# 如果一个Story 对象既有frist_category 字段，又又second_category 字段，为确保Category 对象拥有正确的对象描述符，需要指定relate_name


class Students(models.Model):
    name = models.CharField(max_length=20)


class PsyuanDetail(models.Model):
    name = models.CharField(max_length=8, verbose_name='姓名')
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    gender = models.SmallIntegerField(choices=gender_choices, verbose_name='性别')
    danwei = models.CharField(max_length=100, verbose_name='工作单位')
    psybh = models.CharField(max_length=15, verbose_name='评审员编号')

    class Meta:
        verbose_name = "评审员信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Psyuanb(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓"
                                                        "名")
    psyzc = models.CharField(max_length=10, verbose_name="评审员组成")
    zwzc = models.CharField(max_length=40, verbose_name="职务/职称")
    gzdw = models.CharField(max_length=100, verbose_name="工作单位")
    tel = models.CharField(max_length=15, verbose_name="联系方式")
    psy_detail = models.OneToOneField("PsyuanDetail", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "评审员表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Pingshenxxb(models.Model):
    pstzh = models.CharField(max_length=30, verbose_name='评审通知编号')
    psyh = models.ManyToManyField('Psyuanb')

    class Meta:
        verbose_name = "评审信息总表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pstzh


class Biao4(models.Model):
    # pstzh = models.ForeignKey('Pingshenxxb', on_delete=models.CASCADE)
    lyxh = models.CharField(max_length=20, verbose_name="领域序号")
    lyname = models.CharField(max_length=100, verbose_name="领域")
    lbxh = models.CharField(max_length=20, verbose_name="类别序号")
    lb = models.CharField(max_length=100, verbose_name="类别")
    dxxh = models.CharField(max_length=20, verbose_name="对象序号")
    duixiang = models.CharField(max_length=100, verbose_name="检测对象")
    xmxh = models.CharField(max_length=20, verbose_name="参数序号")
    xmmc = models.CharField(max_length=100, verbose_name="参数名称")
    csmc = models.CharField(max_length=100, verbose_name="参数名称")
    yjbz = models.CharField(max_length=300, verbose_name="依据的标准（方法）名称及编号（含年号）")
    xzfw = models.CharField(max_length=100, verbose_name="限制范围")
    sm = models.CharField(max_length=200, verbose_name="说明")

    class Meta:
        verbose_name = "建议批准的检验检测能力表 表4"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.csmc


class ImportFile(models.Model):
    file = models.FileField(upload_to='File')
    filename = models.CharField(max_length=50, verbose_name='文件名')

    class Meta:
        verbose_name = "文件输入列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.filename


class Biao5(models.Model):
    # pstzh = models.ForeignKey('Pingshenxxb', on_delete=models.CASCADE)  # CASCADE：此值设置，是级联删除。
    name = models.CharField(max_length=10, verbose_name="姓名")
    ziwuzicheng = models.CharField(max_length=30, verbose_name="职务/职称")
    sqqzly = models.CharField(max_length=500, verbose_name="授权签字领域")
    beizu = models.CharField(max_length=300, verbose_name="备注")

    class Meta:
        verbose_name = "建议批准的授权签字人 表5"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
