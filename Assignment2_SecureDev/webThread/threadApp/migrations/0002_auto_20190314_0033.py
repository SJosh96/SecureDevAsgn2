# Generated by Django 2.1.7 on 2019-03-14 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threadApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='threads',
            options={'verbose_name_plural': 'Threads'},
        ),
        migrations.AddField(
            model_name='threads',
            name='thread_Expire',
            field=models.CharField(default='NULL', max_length=200),
        ),
        migrations.AddField(
            model_name='threads',
            name='thread_Exposer',
            field=models.CharField(default='NULL', max_length=200),
        ),
        migrations.AlterField(
            model_name='threads',
            name='created_At',
            field=models.DateTimeField(),
        ),
    ]