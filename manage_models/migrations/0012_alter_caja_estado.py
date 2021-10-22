# Generated by Django 3.2.8 on 2021-10-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_models', '0011_alter_caja_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='estado',
            field=models.CharField(choices=[('A', 'Abierta'), ('C', 'Cerrada')], default='C', max_length=1),
        ),
    ]
