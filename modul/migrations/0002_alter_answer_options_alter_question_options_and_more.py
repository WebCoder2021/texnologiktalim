# Generated by Django 4.1.3 on 2022-11-09 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modul', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Variant', 'verbose_name_plural': 'Variantlar'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['order'], 'verbose_name': 'Test', 'verbose_name_plural': 'Testlar'},
        ),
        migrations.AlterModelOptions(
            name='theme',
            options={'verbose_name': 'Mavzu', 'verbose_name_plural': 'Mavzular'},
        ),
        migrations.AddField(
            model_name='theme',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='modul.module', verbose_name='Modul'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.CharField(max_length=500, verbose_name='Variant'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_true',
            field=models.BooleanField(default=False, verbose_name="To'g'ri yoki xatoligi"),
        ),
        migrations.AlterField(
            model_name='module',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='modules', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='module',
            name='order',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(to='modul.answer', verbose_name='Variantlar'),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(max_length=500, verbose_name='Savol matni'),
        ),
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Savol tartib raqami'),
        ),
        migrations.AlterField(
            model_name='question',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modul.theme', verbose_name='Mavzuni tanlang'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='image',
            field=models.ImageField(upload_to='themes', verbose_name='Mavzu'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Mavzu tartib raqami'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Nomi'),
        ),
    ]
