# Generated by Django 3.2.15 on 2022-12-14 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0005_auto_20221214_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branche',
            name='equipment',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='visits',
        ),
        migrations.AlterField(
            model_name='branche',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='queue',
            name='wait_time',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
