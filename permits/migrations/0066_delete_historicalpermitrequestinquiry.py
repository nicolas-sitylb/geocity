# Generated by Django 3.2.12 on 2022-04-07 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0065_auto_20220406_1421'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricalPermitRequestInquiry',
        ),
    ]
