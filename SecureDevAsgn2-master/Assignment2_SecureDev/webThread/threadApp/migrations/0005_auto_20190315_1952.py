# Generated by Django 2.1.7 on 2019-03-15 23:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('threadApp', '0004_auto_20190315_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='threads',
            name='thread_TillExpire',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='threads',
            name='created_At',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 15, 19, 52, 0, 719442, tzinfo=utc)),
        ),
    ]
