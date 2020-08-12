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

# utf8_general_ci

class Students(models.Model):
    name = models.CharField(max_length=20)


class PsyuanDetail(models.Model):
    name = models.CharField(max_length=8, verbose_name='姓名')
    # gender_choices = (
    #     (0, "女"),
    #     (1, "男"),
    #     (2, "保密"),
    # )
    # gender = models.SmallIntegerField(choices=gender_choices, verbose_name='性别')
    gender = models.CharField(max_length=4, verbose_name="性别")

    danwei = models.CharField(max_length=100, verbose_name='工作单位')
    psybh = models.CharField(max_length=15, verbose_name='评审员编号')

    class Meta:
        verbose_name = "评审员信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Psyuanb(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    psyzc = models.CharField(max_length=10, verbose_name="评审员组成")
    zwzc = models.CharField(max_length=40, verbose_name="职务/职称")
    gzdw = models.CharField(max_length=100, verbose_name="工作单位")
    tel = models.CharField(max_length=15, verbose_name="联系方式")
    psy_detail = models.ForeignKey('PsyuanDetail', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "评审员表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Pstz(models.Model):
    psyzc = models.CharField(max_length=10, verbose_name="评审员组成")
    psname = models.CharField(max_length=10, verbose_name="姓名")
    ziwuzicheng = models.CharField(max_length=30, verbose_name="职务/职称")
    gzdw = models.CharField(max_length=50, verbose_name="工作单位")
    lxfs = models.CharField(max_length=18, verbose_name="联系方式")
    psyuanb = models.ManyToManyField('Psyuanb')


    class Meta:
        verbose_name = "评审组组成表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class Pingshenxxb(models.Model):
    pstzh = models.CharField(max_length=30,verbose_name="评审通知号")
    jcjgmc = models.CharField(max_length=100,verbose_name="检测机构名称")
    psslh = models.CharField(max_length=50,verbose_name="受理号")
    sqsx = models.CharField(max_length=50,verbose_name="申请事项")
    psdate = models.CharField(max_length=30,verbose_name="评审时间")
    psadress = models.CharField(max_length=100,verbose_name="评审地点")
    pstz = models.OneToOneField('Pstz',on_delete=models.CASCADE)

    class Meta:
        verbose_name = "评审信息总表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.psadress


class Biao4(models.Model):
    psxxb = models.ForeignKey('Pingshenxxb', on_delete=models.CASCADE)
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

    importtype = models.CharField(max_length=1, verbose_name='导入类型')
    file = models.FileField(upload_to='File')

    class Meta:
        verbose_name = "文件输入列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.importtype


class Biao5(models.Model):
    psxxb = models.ForeignKey('Pingshenxxb', on_delete=models.CASCADE)  # CASCADE：此值设置，是级联删除。
    xuhao = models.CharField(max_length=2, verbose_name="序号")
    name = models.CharField(max_length=10, verbose_name="姓名")
    ziwuzicheng = models.CharField(max_length=30, verbose_name="职务/职称")
    sqqzly = models.CharField(max_length=500, verbose_name="授权签字领域")
    beizu = models.CharField(max_length=300, verbose_name="备注")

    class Meta:
        verbose_name = "建议批准的授权签字人 表5"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Biao72(models.Model):
    psxxb = models.ForeignKey('Pingshenxxb', on_delete=models.CASCADE)
    xuhao = models.CharField(max_length=4, verbose_name="序号")
    xmmc = models.CharField(max_length=100, verbose_name="检测类别项目或产品名称")
    yjbz = models.CharField(max_length=300, verbose_name="依据标准及代号")
    xmxh = models.CharField(max_length=20, verbose_name="参数序号")
    csmc = models.CharField(max_length=100, verbose_name="参数名称")
    yjbztk = models.CharField(max_length=300, verbose_name="标准条款号")
    xcsy = models.BooleanField(verbose_name="现场试验",default=False)
    nlyz = models.BooleanField(verbose_name="利用能力验证结果",default=False)
    clsh = models.BooleanField(verbose_name="测量审核盲样试验",default=False)
    bdjg = models.BooleanField(verbose_name="利用实验室间比对结果",default=False)
    xcys = models.BooleanField(verbose_name="现场演示",default=False)
    xctw = models.BooleanField(verbose_name="现场提问",default=False)
    cyjlbg = models.BooleanField(verbose_name="查阅记录和报告",default=False)
    hcyq = models.BooleanField(verbose_name="核查仪器设备配置",default=False)
    sfqr = models.BooleanField(verbose_name="是否确认(Y/N)",default=False)
    beizu = models.CharField(max_length=200, verbose_name="备注")

    class Meta:
        verbose_name = "现场评审能力确认方式及确认结果一览表 表7-2"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.csmc



