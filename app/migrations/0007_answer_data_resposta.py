# Generated by Django 2.1 on 2018-08-19 16:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='data_resposta',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]