# Generated by Django 3.0.6 on 2020-05-22 20:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='vector',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=None, size=None),
            preserve_default=False,
        ),
    ]