# Generated by Django 3.2.8 on 2021-10-19 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_models', '0005_alter_usuario_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='domicilio',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='razon_social',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='rfc',
            field=models.CharField(default='', max_length=13),
        ),
    ]
