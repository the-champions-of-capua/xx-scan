# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-20 17:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatOptHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(default='', max_length=155, verbose_name='操作描述')),
                ('type', models.CharField(default='平台日志', max_length=155, verbose_name='操作类型')),
                ('extra', models.CharField(default='', max_length=155, verbose_name='备用字段')),
                ('opreatername', models.CharField(default='actanble', max_length=55, verbose_name='操作者')),
                ('opreate_time', models.DateTimeField(auto_now=True, verbose_name='添加时间')),
                ('conn_file', models.CharField(default='', max_length=255, verbose_name='关联文件')),
                ('remote_file', models.CharField(default='', max_length=255, verbose_name='远程文件')),
            ],
            options={
                'verbose_name': '操作历史记录',
                'ordering': ['-opreate_time'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(default='描述', max_length=255, verbose_name='请求URL')),
                ('truename', models.CharField(default='真实姓名', max_length=55, verbose_name='真实名字')),
                ('identity', models.CharField(choices=[('NetworkManager', '安全管理员'), ('DbUser', '审计员'), ('SuperManager', '管理员')], default='Guest', max_length=50)),
                ('passwd', models.CharField(default='1q2w3e4r', max_length=55, verbose_name='明文密码')),
                ('remarks', models.CharField(default='Guest', max_length=55, verbose_name='备注')),
                ('extra', models.CharField(default='无备注描述', max_length=155, verbose_name='备用字段')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waf', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户信息',
                'db_table': 'userprofile',
            },
        ),
    ]