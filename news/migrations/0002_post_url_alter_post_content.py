# Generated by Django 4.1.3 on 2022-11-19 13:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Kitob url manzili'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Maqola xabari'),
        ),
    ]
