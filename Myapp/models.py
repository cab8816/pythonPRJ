from django.contrib.auth.models import User
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


class ImportFile(models.Model):
    importtype_choices = {
        ('0', u'0_读取评审通知(docx格式)'),
        ('1', u'1_读取评审报告(docx格式)'),
        ('2', u'2_评审员信息表格(docx格式)'),
        ('3', u'3_现场评审核查表(docx格式)'),
    }
    importtype = models.CharField(max_length=1, verbose_name='导入类型', choices=importtype_choices, default=0)
    file = models.FileField(upload_to='File', verbose_name='文件名')
    psxxb = models.ForeignKey('Pingshenxxb', verbose_name='评审信息ID', on_delete=models.CASCADE)  # CASCADE：此值设置，是级联删除。

    class Meta:
        verbose_name = "从文件导入数据"
        verbose_name_plural = verbose_name

    def __str__(self):
        # return self.get_importtype_display()

        return str(self.importtype)


class UserInfo(models.Model):
    username = models.CharField(max_length=150, verbose_name='用户名')
    realname = models.CharField(max_length=10, verbose_name='真名')

    class Meta:
        verbose_name = "用户信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.username)


class PsyuanDetail(models.Model):
    name = models.CharField(max_length=8, verbose_name='姓名')
    gender = models.CharField(max_length=4, verbose_name="性别")
    danwei = models.CharField(max_length=100, verbose_name='工作单位')
    psybh = models.CharField(max_length=15, verbose_name='评审员编号')

    class Meta:
        verbose_name = "评审员个人信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class Pszcy(models.Model):
    psyzc = models.CharField(max_length=10, verbose_name="评审员组成")
    psname = models.CharField(max_length=10, verbose_name="姓名")
    ziwuzicheng = models.CharField(max_length=30, verbose_name="职务/职称")
    gzdw = models.CharField(max_length=50, verbose_name="工作单位")
    lxfs = models.CharField(max_length=18, verbose_name="联系方式")
    psxxbs = models.ManyToManyField('Pingshenxxb', verbose_name="评审通知号")
    psydtl = models.ForeignKey('PsyuanDetail', on_delete=models.CASCADE, verbose_name="评审员信息号", null=True)

    class Meta:
        verbose_name = "评审组名单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class Bpsdwxx(models.Model):
    jyjcjgmc = models.CharField(max_length=100, verbose_name="检验检测机构名称", default="检验检测机构名称")
    zcdz = models.CharField(max_length=100, verbose_name="注册地址", default="注册地址")
    jydz = models.CharField(max_length=100, verbose_name="检验地址", default="检验地址")
    yzbm = models.CharField(max_length=6, verbose_name="邮编", default="邮编")
    chuanz = models.CharField(max_length=20, verbose_name="传真", default="传真")
    email = models.CharField(max_length=50, verbose_name="email", default="email")

    fzr = models.CharField(max_length=10, verbose_name="负责人", default="负责人")
    fzrzw = models.CharField(max_length=20, verbose_name="负责人职务", default="负责人职务")
    fzrgddh = models.CharField(max_length=20, verbose_name="负责人固定电话", default="负责人固定电话")
    fzryddh = models.CharField(max_length=20, verbose_name="负责人移动电话", default="负责人移动电话")

    llr = models.CharField(max_length=10, verbose_name="联络人", default="联络人")
    llrzw = models.CharField(max_length=20, verbose_name="联络人职务", default="联络人职务")
    llrgddh = models.CharField(max_length=20, verbose_name="联络人固定电话", default="联络人固定电话")
    llryddh = models.CharField(max_length=20, verbose_name="联络人移动电话", default="联络人移动电话")

    sfrdw = models.CharField(max_length=100, verbose_name="所属法人单位", default="所属法人单位")
    sfrdwdz = models.CharField(max_length=100, verbose_name="法人单位地址", default="法人单位地址")

    class Meta:
        verbose_name = "被评审单位信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.jyjcjgmc)


class Pingshenxxb(models.Model):
    id = models.AutoField(primary_key=True)
    pstzh = models.CharField(max_length=30, verbose_name="评审通知号", default="评审通知号")
    jcjgmc = models.CharField(max_length=100, verbose_name="检测机构名称", default="检测机构名称")
    psslh = models.CharField(max_length=50, verbose_name="受理号", default="受理号")
    sqsx = models.CharField(max_length=50, verbose_name="申请事项", default="申请事项")
    psdate = models.CharField(max_length=30, verbose_name="评审时间", default="评审时间")
    psadress = models.CharField(max_length=100, verbose_name="评审地点", default="评审地点")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户Id", null=True)
    bpsdwxx = models.ForeignKey('Bpsdwxx', on_delete=models.CASCADE, verbose_name="被评审单位Id", null=True)
    userinfo = models.ManyToManyField('UserInfo')

    class Meta:
        verbose_name = "评审任务信息总表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.pstzh)


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
    xcsy = models.BooleanField(verbose_name="现场试验", default=False)
    nlyz = models.BooleanField(verbose_name="利用能力验证结果", default=False)
    clsh = models.BooleanField(verbose_name="测量审核盲样试验", default=False)
    bdjg = models.BooleanField(verbose_name="利用实验室间比对结果", default=False)
    xcys = models.BooleanField(verbose_name="现场演示", default=False)
    xctw = models.BooleanField(verbose_name="现场提问", default=False)
    cyjlbg = models.BooleanField(verbose_name="查阅记录和报告", default=False)
    hcyq = models.BooleanField(verbose_name="核查仪器设备配置", default=False)
    sfqr = models.BooleanField(verbose_name="是否确认(Y/N)", default=False)
    beizu = models.CharField(max_length=200, verbose_name="备注")

    class Meta:
        verbose_name = "现场评审能力确认方式及确认结果一览表 表7-2"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.csmc


class Xcpshcb(models.Model):
    zhangbh = models.CharField(max_length=3, verbose_name="条款章号")
    zhangmc = models.CharField(max_length=8, verbose_name="条款章名")
    tkhao = models.CharField(max_length=10, verbose_name="条款号")
    psneirong = models.CharField(max_length=1000, verbose_name="评审内容")

    class Meta:
        verbose_name = "检验检测机构资质认定现场评审核查表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tkhao


class Xcpshcb71(models.Model):
    psxxb = models.ForeignKey('Pingshenxxb', verbose_name="评审通知号", on_delete=models.CASCADE, null=True)
    pshcxx = models.ForeignKey('Xcpshcb', verbose_name="核查信息", on_delete=models.CASCADE, null=True)
    psjd = models.CharField(max_length=1, verbose_name="不符合阶段")
    psdate = models.DateField(verbose_name="日期", auto_now=True)
    psjg = models.CharField(max_length=1, verbose_name="评审结果")
    psyj = models.CharField(max_length=500, verbose_name="依据")
    pssm = models.CharField(max_length=500, verbose_name="评审说明")
    jzfs = models.CharField(max_length=1, verbose_name="纠正确认方式")
    bsfyj = models.CharField(max_length=1, verbose_name="被评审方确认意见")
    pszzyj = models.CharField(max_length=1, verbose_name="评审组长确认意见")

    class Meta:
        verbose_name = "现场评审核查表7.1"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.psjg

class Bfhxiang(models.Model):
    psxxb = models.ForeignKey('Pingshenxxb', verbose_name="评审通知号", on_delete=models.CASCADE, null=True)
    bfhxtype_choices = {
        ('0', u'文件评审时完成'),
        ('1', u'现场评审时完成'),
    }
    bfhxwc = models.CharField(max_length=1, verbose_name='完成场所', choices=bfhxtype_choices, default=1)
    bfhxwcdate = models.DateField(verbose_name='完成日期')
    bpsbm = models.CharField(max_length=20,verbose_name='被评审部门')
    ptren = models.CharField(max_length=10,verbose_name='陪同人')
    yiju = models.CharField(max_length=100,verbose_name='依据的管理体系文件/检测标准')
    bfhms = models.CharField(max_length=200,verbose_name='不符合项事实描述')
    bfhjltype_choices = {

        ('0', u'符  合'),
        ('1', u'不符合'),
        ('2', u'不适用'),
    }
    jielun = models.CharField(max_length=10,verbose_name='评审结果',choices=bfhjltype_choices,default=0)
    tkhao = models.CharField(max_length=10,verbose_name='条款号')

    qrfstype_choices = {
        ('0', u'提供必要的见证材料'),
        ('1', u'现场跟踪访问'),
        ('2', u'其他'),
    }
    qrfs = models.CharField(max_length=1, verbose_name='确认方式', choices=qrfstype_choices, default=0)
    psyname = models.CharField(max_length=50,verbose_name='评审员签字')

    qryj_choices = {
        ('0', u'确认'),
        ('1', u'不确认'),
    }
    bfsqueren = models.CharField(max_length=1, verbose_name='被评审方确认意见', choices=qryj_choices, default=0)
    zzqueren  = models.CharField(max_length=1, verbose_name='评审组长确认意见', choices=qryj_choices, default=0)

    class Meta:
        verbose_name = "不符合项记录表6"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tkhao



