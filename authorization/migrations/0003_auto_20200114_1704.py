# Generated by Django 2.2.4 on 2020-01-14 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_auto_20200114_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='course_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='daily',
            name='total_payment',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
