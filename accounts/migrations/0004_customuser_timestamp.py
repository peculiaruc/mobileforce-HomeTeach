# Generated by Django 3.0.8 on 2020-07-08 16:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200708_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
