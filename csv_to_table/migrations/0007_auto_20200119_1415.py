# Generated by Django 2.2 on 2020-01-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_to_table', '0006_auto_20200119_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
