# Generated by Django 2.1 on 2018-08-16 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_dadosempresa_nome_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questao', models.CharField(max_length=500)),
                ('texto', models.TextField()),
            ],
        ),
    ]