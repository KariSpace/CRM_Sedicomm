# Generated by Django 2.2 on 2020-01-20 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_to_table', '0008_auto_20200119_2350'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='people',
            name='csv_to_tabl_date_4ab4e2_idx',
        ),
    ]
