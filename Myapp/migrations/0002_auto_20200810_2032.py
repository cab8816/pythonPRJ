# Generated by Django 2.0 on 2020-08-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psyuandetail',
            name='gender',
            field=models.CharField(max_length=4, verbose_name='性别'),
        ),
    ]
