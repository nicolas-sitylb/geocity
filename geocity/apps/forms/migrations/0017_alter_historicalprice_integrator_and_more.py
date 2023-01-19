# Generated by Django 4.1.4 on 2023-01-19 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("forms", "0016_alter_historicalprice_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalprice",
            name="integrator",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                limit_choices_to={"permit_department__is_integrator_admin": True},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="auth.group",
                verbose_name="Groupe des administrateurs",
            ),
        ),
        migrations.AlterField(
            model_name="paymentsettings",
            name="integrator",
            field=models.ForeignKey(
                limit_choices_to={"permit_department__is_integrator_admin": True},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="auth.group",
                verbose_name="Groupe des administrateurs",
            ),
        ),
        migrations.AlterField(
            model_name="price",
            name="integrator",
            field=models.ForeignKey(
                limit_choices_to={"permit_department__is_integrator_admin": True},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="auth.group",
                verbose_name="Groupe des administrateurs",
            ),
        ),
    ]
