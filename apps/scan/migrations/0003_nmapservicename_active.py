# Generated by Django 2.1.7 on 2019-05-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0002_auto_20190524_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='nmapservicename',
            name='active',
            field=models.BooleanField(default=True, verbose_name='激活.当前有工具的状态'),
        ),
    ]
