# Generated by Django 3.2.8 on 2021-10-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_models', '0009_auto_20211021_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='estado',
            field=models.CharField(choices=[('A', 'Abierta'), ('C', 'Cerrada')], default=('A', 'Abierta'), max_length=1),
        ),
    ]
