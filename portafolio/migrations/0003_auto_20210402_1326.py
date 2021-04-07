# Generated by Django 3.1.7 on 2021-04-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0002_auto_20210402_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='madre',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='padre',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='slug',
        ),
        migrations.AddField(
            model_name='producto',
            name='madre',
            field=models.CharField(max_length=50, null=True, verbose_name='Madre'),
        ),
        migrations.AddField(
            model_name='producto',
            name='padre',
            field=models.CharField(max_length=50, null=True, verbose_name='Padre'),
        ),
    ]