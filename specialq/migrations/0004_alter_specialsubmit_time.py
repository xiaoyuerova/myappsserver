# Generated by Django 4.1 on 2023-05-04 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialq', '0003_alter_specialsubmit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialsubmit',
            name='time',
            field=models.TimeField(default=datetime.time(12, 17, 7, 840907), verbose_name='提交时间'),
        ),
    ]
