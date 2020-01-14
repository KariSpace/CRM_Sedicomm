# Generated by Django 2.2.4 on 2020-01-14 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='callback_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='daily',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='daily',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='daily',
            name='course',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='daily',
            name='course_price',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='daily',
            name='currency',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='daily',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='daily',
            name='group',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='daily',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='daily',
            name='obligation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='daily',
            name='payment_history',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='daily',
            name='payment_source',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='daily',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='daily',
            name='request_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='daily',
            name='request_status',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='daily',
            name='total_payment',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='daily',
            name='university',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='daily',
            name='where_from',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='daily',
            name='wishes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='daily',
            name='work',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
