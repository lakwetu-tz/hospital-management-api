# Generated by Django 3.2.15 on 2022-12-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0006_auto_20221214_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
    ]
