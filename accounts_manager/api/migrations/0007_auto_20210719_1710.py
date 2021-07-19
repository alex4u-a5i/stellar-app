# Generated by Django 3.2.5 on 2021-07-19 16:10

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210712_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=api.models.generate_unique_code, max_length=8, unique=True)),
                ('XDR', models.CharField(max_length=1000)),
                ('notes', models.CharField(blank=True, max_length=1000)),
                ('available_to_sign', models.BooleanField()),
                ('total_signature_weight', models.IntegerField()),
                ('completed', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='code',
        ),
        migrations.AddField(
            model_name='account',
            name='public_key',
            field=models.CharField(default='', max_length=56, unique=True),
        ),
        migrations.AddField(
            model_name='accountuser',
            name='account',
            field=models.ManyToManyField(to='api.Account'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.DeleteModel(
            name='Token',
        ),
        migrations.AddField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.account'),
        ),
    ]
