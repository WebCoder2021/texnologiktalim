# Generated by Django 4.1.3 on 2022-11-15 05:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500, verbose_name='Variant')),
                ('is_true', models.BooleanField(default=False, verbose_name="To'g'ri yoki xatoligi")),
            ],
            options={
                'verbose_name': 'Variant',
                'verbose_name_plural': 'Variantlar',
            },
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Savol matni')),
                ('answers', models.ManyToManyField(to='all_test.testanswer', verbose_name='Variantlar')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Testlar',
            },
        ),
    ]
