# Generated by Django 4.2.16 on 2024-10-20 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_productmodel_sizes_delete_sizemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128, verbose_name='Color name')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='Color code')),
            ],
            options={
                'verbose_name': 'Colour',
                'verbose_name_plural': 'Colours',
            },
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='colours',
        ),
        migrations.DeleteModel(
            name='ColourModel',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='colors',
            field=models.ManyToManyField(related_name='products', to='products.colormodel'),
        ),
    ]
