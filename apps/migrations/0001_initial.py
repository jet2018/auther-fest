# Generated by Django 3.2.12 on 2022-05-05 07:02

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
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=100, unique=True)),
                ('redirect_to_url', models.URLField()),
                ('app_icon', models.ImageField(blank=True, null=True, upload_to='icons')),
                ('app_category', models.CharField(max_length=80)),
                ('app_access_data', models.CharField(max_length=300)),
                ('app_public_key', models.CharField(max_length=300, unique=True)),
                ('app_secret_key', models.CharField(max_length=100, unique=True)),
                ('app_secret_key_hash', models.CharField(max_length=300)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AllowedApps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('allowed_on', models.DateTimeField(auto_now=True)),
                ('number_of_logins', models.PositiveIntegerField(default=0)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.app')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]