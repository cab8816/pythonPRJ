# Generated by Django 3.1.2 on 2020-11-05 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_auto_20201101_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importfile',
            name='importtype',
            field=models.CharField(choices=[('2', '2_评审员信息表格(docx格式)'), ('0', '0_读取评审通知(docx格式)'), ('3', '3_现场评审核查表(docx格式)'), ('1', '1_读取评审报告(docx格式)')], default=0, max_length=1, verbose_name='导入类型'),
        ),
        migrations.CreateModel(
            name='Bfhxiang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bfhxwc', models.CharField(choices=[('0', '文件评审时完成'), ('1', '现场评审时完成')], default=1, max_length=1, verbose_name='完成场所')),
                ('bfhxwcdate', models.DateField(verbose_name='完成日期')),
                ('bpsbm', models.CharField(max_length=20, verbose_name='被评审部门')),
                ('ptren', models.CharField(max_length=10, verbose_name='陪同人')),
                ('yiju', models.CharField(max_length=100, verbose_name='依据的管理体系文件/检测标准')),
                ('bfhms', models.CharField(max_length=200, verbose_name='不符合项事实描述')),
                ('jielun', models.CharField(choices=[('1', '不适用'), ('0', '不符合')], default=0, max_length=10, verbose_name='评审结果')),
                ('tkhao', models.CharField(max_length=10, verbose_name='条款号')),
                ('qrfs', models.CharField(choices=[('0', '提供必要的见证材料'), ('1', '现场跟踪访问'), ('2', '其他')], default=0, max_length=1, verbose_name='确认方式')),
                ('psyname', models.CharField(max_length=50, verbose_name='评审员签字')),
                ('bfsqueren', models.CharField(choices=[('0', '确认'), ('1', '不确认')], default=0, max_length=1, verbose_name='被评审方确认意见')),
                ('zzqueren', models.CharField(choices=[('0', '确认'), ('1', '不确认')], default=0, max_length=1, verbose_name='评审组长确认意见')),
                ('psxxb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Myapp.pingshenxxb', verbose_name='评审通知号')),
            ],
            options={
                'verbose_name': '不符合项记录表6',
                'verbose_name_plural': '不符合项记录表6',
            },
        ),
    ]