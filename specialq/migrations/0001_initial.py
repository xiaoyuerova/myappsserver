# Generated by Django 4.1 on 2023-05-04 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialSubmit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WjId', models.IntegerField(verbose_name='关联问卷id')),
                ('Number', models.IntegerField(verbose_name='第number位提交的人')),
                ('Data', models.DateField(default=datetime.date(2023, 5, 4), verbose_name='提交日期')),
                ('time', models.TimeField(default=datetime.time(9, 15, 2, 490083), verbose_name='提交时间')),
                ('SubmitIp', models.CharField(max_length=15, verbose_name='提交ip')),
                ('UseTime', models.IntegerField(verbose_name='填写用时')),
                ('Agent', models.CharField(max_length=100, verbose_name='提交客户端')),
                ('Answer', models.CharField(max_length=50, verbose_name='提交的答案')),
            ],
        ),
    ]
