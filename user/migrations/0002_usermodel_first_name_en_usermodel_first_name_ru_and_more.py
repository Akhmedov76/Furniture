# Generated by Django 4.2.16 on 2024-10-21 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='first_name_en',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='first_name_ru',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='first_name_uz',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='last_name_en',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='last_name_ru',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='last_name_uz',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
