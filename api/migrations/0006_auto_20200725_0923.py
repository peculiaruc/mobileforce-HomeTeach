# Generated by Django 3.0.8 on 2020-07-25 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200725_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='day',
            field=models.DateField(),
        ),
    ]
