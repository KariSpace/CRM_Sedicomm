# Generated by Django 2.2 on 2020-01-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('course', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('university', models.CharField(blank=True, max_length=50)),
                ('work', models.CharField(blank=True, max_length=50)),
                ('where_from', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]