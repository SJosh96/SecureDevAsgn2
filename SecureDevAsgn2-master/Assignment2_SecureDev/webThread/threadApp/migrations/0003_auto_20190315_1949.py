# Generated by Django 2.1.7 on 2019-03-15 23:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('threadApp', '0002_auto_20190315_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='threads',
            name='thread_TillExpire',
        ),
        migrations.AlterField(
            model_name='threads',
            name='created_At',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 15, 19, 49, 8, 860943, tzinfo=utc)),
        ),
    ]