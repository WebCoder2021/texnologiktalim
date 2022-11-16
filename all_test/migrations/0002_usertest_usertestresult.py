# Generated by Django 4.1.3 on 2022-11-15 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('all_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_test.testanswer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_test.testquestion')),
            ],
        ),
        migrations.CreateModel(
            name='UserTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('tests', models.ManyToManyField(to='all_test.usertest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]