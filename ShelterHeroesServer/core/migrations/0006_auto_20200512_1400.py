# Generated by Django 3.0.5 on 2020-05-12 14:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200512_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created'),
        ),
    ]
