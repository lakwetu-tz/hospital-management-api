# Generated by Django 3.2.15 on 2022-12-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0002_auto_20221214_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='title',
            field=models.TextField(max_length=20, null=True),
        ),
    ]
