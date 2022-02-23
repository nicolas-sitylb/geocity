# Generated by Django 3.2.7 on 2022-02-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0058_filter_qgs_file_extension'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksobject',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='ordre'),
        ),
        migrations.AlterModelOptions(
            name='worksobject',
            options={'ordering': ['order'], 'verbose_name': "1.3 Configuration de l'objet", 'verbose_name_plural': '1.3 Configuration des objets'},
        ),
    ]
