# Generated by Django 4.1.4 on 2023-02-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0022_style_page"),
    ]

    operations = [
        migrations.AlterField(
            model_name="style",
            name="page",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Toutes les pages"),
                    (1, "Première page"),
                    (2, "Toutes sauf la première page"),
                ],
                default=0,
                help_text="Choix des pages auxquelles doit s'appliquer le style",
                verbose_name="Page",
            ),
        ),
    ]
