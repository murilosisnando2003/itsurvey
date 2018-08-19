# Generated by Django 2.1 on 2018-08-19 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180817_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='resposta',
        ),
        migrations.AddField(
            model_name='question',
            name='empresa',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Empresa', verbose_name='related empresa'),
            preserve_default=False,
        ),
    ]
