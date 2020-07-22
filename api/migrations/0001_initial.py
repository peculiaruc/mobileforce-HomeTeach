# Generated by Django 3.0.8 on 2020-07-19 22:25

import api.models
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
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('reference', models.CharField(max_length=150)),
                ('authorization_code', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_balance', models.IntegerField(default=0)),
                ('total_balance', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_hour', models.CharField(max_length=10)),
                ('from_minute', models.CharField(max_length=10)),
                ('to_hour', models.CharField(max_length=10)),
                ('to_minute', models.CharField(max_length=10)),
                ('days', models.ManyToManyField(blank=True, null=True, to='api.Days')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('declined', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=False)),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pending_requests', to=settings.AUTH_USER_MODEL)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.StudentSchedule')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings_tutor', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, default='default/default.jpg', null=True, upload_to=api.models.get_upload_file_name)),
                ('credentials', models.FileField(blank=True, null=True, upload_to=api.models.get_upload_file_name_credentials)),
                ('video', models.FileField(blank=True, null=True, upload_to=api.models.get_upload_file_name_videos)),
                ('desc', models.TextField(blank=True, max_length=255, null=True)),
                ('field', models.CharField(blank=True, max_length=255)),
                ('hourly_rate', models.CharField(default=0, max_length=10000000)),
                ('major_course', models.CharField(blank=True, max_length=255, null=True)),
                ('other_courses', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.ManyToManyField(blank=True, to='api.Rating')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCardInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_holder_name', models.CharField(max_length=255, null=True)),
                ('card_number', models.CharField(max_length=255, null=True)),
                ('cvv', models.CharField(max_length=255, null=True)),
                ('expiry_month', models.IntegerField(null=True)),
                ('expiry_year', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BankInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, max_length=255, null=True)),
                ('account_name', models.CharField(blank=True, max_length=255, null=True)),
                ('account_number', models.IntegerField(blank=True, null=True)),
                ('routing_number', models.IntegerField(blank=True, null=True)),
                ('social_security_number', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
