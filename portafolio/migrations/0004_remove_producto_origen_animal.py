# Generated by Django 3.1.7 on 2021-04-02 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0003_auto_20210402_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='origen_animal',
        ),
    ]
