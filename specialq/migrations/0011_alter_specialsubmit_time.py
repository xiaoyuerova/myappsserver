# Generated by Django 4.1 on 2023-05-12 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialq', '0010_alter_specialsubmit_time_alter_specialsubmit_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialsubmit',
            name='Time',
            field=models.TimeField(default=datetime.time(14, 7, 17, 167478), verbose_name='提交时间'),
        ),
    ]
