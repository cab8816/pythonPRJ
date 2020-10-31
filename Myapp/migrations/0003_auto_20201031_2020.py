# Generated by Django 3.1.2 on 2020-10-31 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_auto_20201031_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importfile',
            name='importtype',
            field=models.CharField(choices=[('2', '2_评审员信息表格(docx格式)'), ('3', '3_现场评审核查表(docx格式)'), ('0', '0_读取评审通知(docx格式)'), ('1', '1_读取评审报告(docx格式)')], default=0, max_length=1, verbose_name='导入类型'),
        ),
        migrations.AlterField(
            model_name='pingshenxxb',
            name='id',
            field=models.IntegerField(max_length=11, primary_key=True, serialize=False, verbose_name='序号'),
        ),
    ]
