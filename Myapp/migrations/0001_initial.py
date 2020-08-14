# Generated by Django 2.0 on 2020-08-14 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biao4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyxh', models.CharField(max_length=20, verbose_name='领域序号')),
                ('lyname', models.CharField(max_length=100, verbose_name='领域')),
                ('lbxh', models.CharField(max_length=20, verbose_name='类别序号')),
                ('lb', models.CharField(max_length=100, verbose_name='类别')),
                ('dxxh', models.CharField(max_length=20, verbose_name='对象序号')),
                ('duixiang', models.CharField(max_length=100, verbose_name='检测对象')),
                ('xmxh', models.CharField(max_length=20, verbose_name='参数序号')),
                ('xmmc', models.CharField(max_length=100, verbose_name='参数名称')),
                ('csmc', models.CharField(max_length=100, verbose_name='参数名称')),
                ('yjbz', models.CharField(max_length=300, verbose_name='依据的标准（方法）名称及编号（含年号）')),
                ('xzfw', models.CharField(max_length=100, verbose_name='限制范围')),
                ('sm', models.CharField(max_length=200, verbose_name='说明')),
            ],
            options={
                'verbose_name': '建议批准的检验检测能力表 表4',
                'verbose_name_plural': '建议批准的检验检测能力表 表4',
            },
        ),
        migrations.CreateModel(
            name='Biao5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xuhao', models.CharField(max_length=2, verbose_name='序号')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('ziwuzicheng', models.CharField(max_length=30, verbose_name='职务/职称')),
                ('sqqzly', models.CharField(max_length=500, verbose_name='授权签字领域')),
                ('beizu', models.CharField(max_length=300, verbose_name='备注')),
            ],
            options={
                'verbose_name': '建议批准的授权签字人 表5',
                'verbose_name_plural': '建议批准的授权签字人 表5',
            },
        ),
        migrations.CreateModel(
            name='Biao72',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xuhao', models.CharField(max_length=4, verbose_name='序号')),
                ('xmmc', models.CharField(max_length=100, verbose_name='检测类别项目或产品名称')),
                ('yjbz', models.CharField(max_length=300, verbose_name='依据标准及代号')),
                ('xmxh', models.CharField(max_length=20, verbose_name='参数序号')),
                ('csmc', models.CharField(max_length=100, verbose_name='参数名称')),
                ('yjbztk', models.CharField(max_length=300, verbose_name='标准条款号')),
                ('xcsy', models.BooleanField(default=False, verbose_name='现场试验')),
                ('nlyz', models.BooleanField(default=False, verbose_name='利用能力验证结果')),
                ('clsh', models.BooleanField(default=False, verbose_name='测量审核盲样试验')),
                ('bdjg', models.BooleanField(default=False, verbose_name='利用实验室间比对结果')),
                ('xcys', models.BooleanField(default=False, verbose_name='现场演示')),
                ('xctw', models.BooleanField(default=False, verbose_name='现场提问')),
                ('cyjlbg', models.BooleanField(default=False, verbose_name='查阅记录和报告')),
                ('hcyq', models.BooleanField(default=False, verbose_name='核查仪器设备配置')),
                ('sfqr', models.BooleanField(default=False, verbose_name='是否确认(Y/N)')),
                ('beizu', models.CharField(max_length=200, verbose_name='备注')),
            ],
            options={
                'verbose_name': '现场评审能力确认方式及确认结果一览表 表7-2',
                'verbose_name_plural': '现场评审能力确认方式及确认结果一览表 表7-2',
            },
        ),
        migrations.CreateModel(
            name='ImportFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importtype', models.CharField(max_length=1, verbose_name='导入类型')),
                ('file', models.FileField(upload_to='File')),
            ],
            options={
                'verbose_name': '文件输入列表',
                'verbose_name_plural': '文件输入列表',
            },
        ),
        migrations.CreateModel(
            name='Pingshenxxb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pstzh', models.CharField(default='评审通知号', max_length=30, verbose_name='评审通知号')),
                ('jcjgmc', models.CharField(default='检测机构名称', max_length=100, verbose_name='检测机构名称')),
                ('psslh', models.CharField(default='受理号', max_length=50, verbose_name='受理号')),
                ('sqsx', models.CharField(default='申请事项', max_length=50, verbose_name='申请事项')),
                ('psdate', models.CharField(default='评审时间', max_length=30, verbose_name='评审时间')),
                ('psadress', models.CharField(default='评审地点', max_length=100, verbose_name='评审地点')),
            ],
            options={
                'verbose_name': '评审信息总表',
                'verbose_name_plural': '评审信息总表',
            },
        ),
        migrations.CreateModel(
            name='PsyuanDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name='姓名')),
                ('gender', models.CharField(max_length=4, verbose_name='性别')),
                ('danwei', models.CharField(max_length=100, verbose_name='工作单位')),
                ('psybh', models.CharField(max_length=15, verbose_name='评审员编号')),
            ],
            options={
                'verbose_name': '评审员信息表',
                'verbose_name_plural': '评审员信息表',
            },
        ),
        migrations.CreateModel(
            name='Pszcy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psyzc', models.CharField(max_length=10, verbose_name='评审员组成')),
                ('psname', models.CharField(max_length=10, verbose_name='姓名')),
                ('ziwuzicheng', models.CharField(max_length=30, verbose_name='职务/职称')),
                ('gzdw', models.CharField(max_length=50, verbose_name='工作单位')),
                ('lxfs', models.CharField(max_length=18, verbose_name='联系方式')),
                ('psxxb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.Pingshenxxb', verbose_name='评审通知号')),
                ('psydtl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.PsyuanDetail', verbose_name='评审员信息号')),
            ],
            options={
                'verbose_name': '评审组组成表',
                'verbose_name_plural': '评审组组成表',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='biao72',
            name='psxxb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.Pingshenxxb'),
        ),
        migrations.AddField(
            model_name='biao5',
            name='psxxb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.Pingshenxxb'),
        ),
        migrations.AddField(
            model_name='biao4',
            name='psxxb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.Pingshenxxb'),
        ),
    ]
