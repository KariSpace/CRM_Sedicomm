# Generated by Django 2.2.4 on 2020-02-07 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0005_auto_20200207_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily',
            name='need_confirm',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='need_confirm',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]