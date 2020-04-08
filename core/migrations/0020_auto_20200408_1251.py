# Generated by Django 2.2 on 2020-04-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20200406_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='being_delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='granted_refund',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='request_refund',
            field=models.BooleanField(default=False),
        ),
    ]
