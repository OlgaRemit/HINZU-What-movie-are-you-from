# Generated by Django 3.0.6 on 2020-05-22 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='embed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_embed', to='service.Embed'),
        ),
    ]
