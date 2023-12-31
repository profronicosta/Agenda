# Generated by Django 4.2.7 on 2023-11-01 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaApp', '0003_alter_contato_bairro_alter_contato_data_nascimento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('uf', models.CharField(choices=[('SP', 'São Paulo'), ('MG', 'Minas Gerais'), ('RJ', 'Rio de Janeiro'), ('ES', 'Espírito Santo')], max_length=2)),
            ],
        ),
    ]
