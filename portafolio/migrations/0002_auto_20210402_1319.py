# Generated by Django 3.1.7 on 2021-04-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='madre',
            field=models.CharField(max_length=50, null=True, verbose_name='Madre'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='padre',
            field=models.CharField(max_length=50, null=True, verbose_name='Padre'),
        ),
    ]
