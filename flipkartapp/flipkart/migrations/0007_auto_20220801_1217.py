# Generated by Django 3.1.14 on 2022-08-01 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0006_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 1, 12, 17, 18, 465023)),
        ),
    ]
