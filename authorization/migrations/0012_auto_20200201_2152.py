# Generated by Django 2.2.4 on 2020-02-01 19:52

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0011_auto_20200126_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='group',
            field=jsonfield.fields.JSONField(blank=True),
        ),
    ]
