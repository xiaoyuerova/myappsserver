# Generated by Django 4.1 on 2023-05-04 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialq', '0005_remove_specialsubmit_time_specialsubmit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialsubmit',
            name='Agent',
            field=models.CharField(max_length=300, verbose_name='提交客户端'),
        ),
        migrations.AlterField(
            model_name='specialsubmit',
            name='Time',
            field=models.TimeField(default=datetime.time(12, 59, 58, 860829), verbose_name='提交时间'),
        ),
    ]
