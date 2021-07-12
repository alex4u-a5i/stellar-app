# Generated by Django 3.2.5 on 2021-07-12 19:01

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210710_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountuser',
            name='account',
        ),
        migrations.AlterField(
            model_name='account',
            name='code',
            field=models.CharField(default=api.models.generate_unique_code, max_length=8, unique=True),
        ),
    ]
