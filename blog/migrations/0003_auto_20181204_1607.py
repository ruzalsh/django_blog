# Generated by Django 2.1.3 on 2018-12-04 10:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181204_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 4, 10, 22, 36, 946433, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 4, 10, 22, 36, 944550, tzinfo=utc)),
        ),
    ]
