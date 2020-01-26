# Generated by Django 2.2.4 on 2020-01-24 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0009_auto_20200124_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('course', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('university', models.CharField(blank=True, max_length=100)),
                ('work', models.CharField(blank=True, max_length=100)),
                ('where_from', models.CharField(blank=True, max_length=100)),
                ('currency', models.CharField(blank=True, max_length=100)),
                ('course_price', models.IntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True)),
                ('wishes', models.TextField(blank=True)),
                ('callback_time', models.DateTimeField(blank=True, null=True)),
                ('group', models.CharField(blank=True, max_length=100)),
                ('request_status', models.CharField(blank=True, max_length=100)),
                ('payment_history', models.TextField(blank=True)),
                ('total_payment', models.IntegerField(blank=True, null=True)),
                ('payment_source', models.CharField(blank=True, max_length=100)),
                ('obligation', models.IntegerField(blank=True, null=True)),
                ('date_added', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveIndex(
            model_name='groups',
            name='authorizati_request_fdee7b_idx',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='callback_time',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='country',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='course',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='course_price',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='email',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='obligation',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='payment_history',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='payment_source',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='request_date',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='request_status',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='total_payment',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='university',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='where_from',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='wishes',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='work',
        ),
        migrations.AddField(
            model_name='groups',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='groups',
            name='time_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='groups',
            name='time_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddIndex(
            model_name='group',
            index=models.Index(fields=['group'], name='authorizati_group_5a4748_idx'),
        ),
    ]
