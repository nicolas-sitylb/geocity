# Generated by Django 3.2.12 on 2022-04-12 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('permits', '0071_delete_historicalpermitrequestinquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivedPermitRequest',
            fields=[
                ('archived_date', models.DateTimeField()),
                ('permit_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='permits.permitrequest')),
                ('archivist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Personne ayant archivé la demande')),
            ],
        ),
    ]
