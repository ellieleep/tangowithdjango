# Generated by Django 3.2.5 on 2021-08-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]