# Generated by Django 4.2.6 on 2023-11-02 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaApp', '0006_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefone',
            name='ddd',
            field=models.IntegerField(),
        ),
    ]
