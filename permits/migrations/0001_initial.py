# Generated by Django 2.2.13 on 2020-09-25 12:13

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import permits.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeomLayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layer_name', models.CharField(blank=True, max_length=128, verbose_name='Nom de la couche source')),
                ('description', models.CharField(blank=True, max_length=1024, verbose_name='Commentaire')),
                ('source_id', models.CharField(blank=True, max_length=128, verbose_name='Id entité')),
                ('source_subid', models.CharField(blank=True, max_length=128, verbose_name='Id entité secondaire')),
                ('external_link', models.URLField(blank=True, verbose_name='Lien externe')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=2056, verbose_name='Géométrie')),
            ],
            options={
                'verbose_name': "3.4 Consultation de l'entité géographique à intersecter",
                'verbose_name_plural': '3.4 Consultation des entités géographiques à intersecter',
            },
        ),
        migrations.CreateModel(
            name='PermitActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=100, verbose_name='Nom')),
                ('company_name', models.CharField(max_length=100, verbose_name='Entreprise')),
                ('vat_number', models.CharField(blank=True, max_length=19, verbose_name='Numéro TVA')),
                ('address', models.CharField(max_length=100, verbose_name='Adresse')),
                ('zipcode', models.PositiveIntegerField(verbose_name='NPA')),
                ('city', models.CharField(max_length=100, verbose_name='Ville')),
                ('phone', models.CharField(max_length=20, verbose_name='Téléphone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='PermitAdministrativeEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('ofs_id', models.PositiveIntegerField(verbose_name='ofs_id')),
                ('archive_link', models.URLField(blank=True, max_length=1024, verbose_name='Archives externes')),
                ('legal_document', permits.fields.AministrativeEntityFileField(blank=True, storage=permits.fields.PrivateFileSystemStorage(), upload_to='administrative_entity_files/', verbose_name='Directive')),
                ('general_informations', models.CharField(blank=True, max_length=1024, verbose_name='Informations')),
                ('link', models.URLField(blank=True, verbose_name='Lien')),
                ('logo_main', permits.fields.AministrativeEntityFileField(blank=True, storage=permits.fields.PrivateFileSystemStorage(), upload_to='administrative_entity_files/', verbose_name='Logo principal')),
                ('logo_secondary', permits.fields.AministrativeEntityFileField(blank=True, storage=permits.fields.PrivateFileSystemStorage(), upload_to='administrative_entity_files/', verbose_name='Logo secondaire')),
                ('title_signature_1', models.CharField(blank=True, max_length=128, verbose_name='Signature Gauche')),
                ('image_signature_1', permits.fields.AministrativeEntityFileField(blank=True, storage=permits.fields.PrivateFileSystemStorage(), upload_to='administrative_entity_files/', verbose_name='Signature gauche')),
                ('title_signature_2', models.CharField(blank=True, max_length=128, verbose_name='Signature Droite')),
                ('image_signature_2', permits.fields.AministrativeEntityFileField(blank=True, storage=permits.fields.PrivateFileSystemStorage(), upload_to='administrative_entity_files/', verbose_name='Signature droite')),
                ('phone', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message='Seuls les chiffres et les espaces sont autorisés.', regex='^(((\\+41)\\s?)|(0))?(\\d{2})\\s?(\\d{3})\\s?(\\d{2})\\s?(\\d{2})$')], verbose_name='Téléphone')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=2056, verbose_name='geom')),
            ],
            options={
                'verbose_name': "1.1 Configuration de l'entité administrative (commune, organisation)",
                'verbose_name_plural': "1.1 Configuration de l'entité administrative (commune, organisation)",
            },
        ),
        migrations.CreateModel(
            name='PermitAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100, verbose_name='Raison Sociale')),
                ('vat_number', models.CharField(blank=True, max_length=19, validators=[django.core.validators.RegexValidator(message="Le code d'entreprise doit être de type                          CHE-123.456.789 (TVA)                          et vous pouvez le trouver sur                          le registe fédéral des entreprises                          https://www.uid.admin.ch/search.aspx", regex='^(CHE-)+\\d{3}\\.\\d{3}\\.\\d{3}(\\sTVA)?$')], verbose_name='Numéro TVA')),
                ('address', models.CharField(max_length=100, verbose_name='Rue')),
                ('zipcode', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)], verbose_name='NPA')),
                ('city', models.CharField(max_length=100, verbose_name='Ville')),
                ('phone_first', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Seuls les chiffres et les espaces sont autorisés.', regex='^(((\\+41)\\s?)|(0))?(\\d{2})\\s?(\\d{3})\\s?(\\d{2})\\s?(\\d{2})$')], verbose_name='Téléphone principal')),
                ('phone_second', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message='Seuls les chiffres et les espaces sont autorisés.', regex='^(((\\+41)\\s?)|(0))?(\\d{2})\\s?(\\d{3})\\s?(\\d{2})\\s?(\\d{2})$')], verbose_name='Téléphone secondaire')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "3.2 Consultation de l'auteur",
                'verbose_name_plural': '3.2 Consultation des auteurs',
            },
        ),
        migrations.CreateModel(
            name='PermitDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='Service', max_length=100, verbose_name='description')),
                ('is_validator', models.BooleanField(verbose_name='is_validator')),
                ('is_admin', models.BooleanField(verbose_name='is_admin')),
                ('is_archeologist', models.BooleanField(verbose_name='is_archeologist')),
                ('is_default_validator', models.BooleanField(default=False, verbose_name='sélectionné par défaut pour les validations')),
                ('administrative_entity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departments', to='permits.PermitAdministrativeEntity', verbose_name='permit_administrative_entity')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'verbose_name': '2.1 Configuration du service (pilote, validateur...)',
                'verbose_name_plural': '2.1 Configuration des services (pilote, validateur...)',
            },
        ),
        migrations.CreateModel(
            name='PermitRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Brouillon'), (1, 'Envoyée, en attente de traitement'), (4, 'Demande de compléments'), (3, 'En traitement'), (5, 'En validation'), (2, 'Approuvée'), (6, 'Refusée')], default=0, verbose_name='état')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date de création')),
                ('validated_at', models.DateTimeField(null=True, verbose_name='date de validation')),
                ('printed_at', models.DateTimeField(null=True, verbose_name="date d'impression")),
                ('printed_by', models.CharField(blank=True, max_length=255, verbose_name='imprimé par')),
                ('printed_file', permits.fields.AministrativeEntityFileField(blank=True, null=True, storage=permits.fields.PrivateFileSystemStorage(), upload_to='printed_permits/', verbose_name='Permis imprimé')),
                ('archeology_status', models.PositiveSmallIntegerField(choices=[(0, 'Non pertinent'), (1, 'Inconnu'), (2, 'Pas fouillé'), (3, 'Partiellement fouillé'), (4, 'Déjà fouillé')], default=0, verbose_name='Statut archéologique')),
                ('intersected_geometries', models.CharField(max_length=1024, null=True, verbose_name='Entités géométriques concernées')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Émolument')),
                ('exemption', models.TextField(blank=True, verbose_name='Dérogation')),
                ('opposition', models.TextField(blank=True, verbose_name='Opposition')),
                ('comment', models.TextField(blank=True, verbose_name='Analyse du service pilote')),
                ('validation_pdf', permits.fields.PermitRequestFileField(storage=permits.fields.PrivateFileSystemStorage(), upload_to='validations', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='pdf de validation')),
                ('creditor_type', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Autres'), (2, 'Propriétaire'), (3, 'Entreprise'), (4, "Maître d'ouvrage"), (1, "Requérant si différent de l'auteur de la demande"), (5, 'Sécurité'), (6, 'Association')], null=True, verbose_name='Destinaire de la facture')),
            ],
            options={
                'verbose_name': '3.1 Consultation de la demande',
                'verbose_name_plural': '3.1 Consultation des demandes',
                'permissions': [('amend_permit_request', 'Traiter les demandes'), ('validate_permit_request', 'Valider les demandes'), ('classify_permit_request', 'Classer les demandes')],
            },
        ),
        migrations.CreateModel(
            name='WorksObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nom')),
            ],
            options={
                'verbose_name': "1.3 Configuration de l'objet",
                'verbose_name_plural': '1.3 Configuration des objets',
            },
        ),
        migrations.CreateModel(
            name='WorksObjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrative_entities', models.ManyToManyField(related_name='works_object_types', to='permits.PermitAdministrativeEntity', verbose_name='communes')),
                ('works_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works_object_types', to='permits.WorksObject', verbose_name='objet des travaux')),
            ],
            options={
                'verbose_name': '1.4 Configuration type-objet-entité administrative',
                'verbose_name_plural': '1.4 Configurations type-objet-entité administrative',
            },
        ),
        migrations.CreateModel(
            name='WorksType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nom')),
            ],
            options={
                'verbose_name': '1.2 Configuration du type',
                'verbose_name_plural': '1.2 Configuration des types',
            },
        ),
        migrations.CreateModel(
            name='WorksObjectTypeChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permit_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permits.PermitRequest')),
                ('works_object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permits.WorksObjectType')),
            ],
            options={
                'unique_together': {('permit_request', 'works_object_type')},
            },
        ),
        migrations.AddField(
            model_name='worksobjecttype',
            name='works_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works_object_types', to='permits.WorksType', verbose_name='type de travaux'),
        ),
        migrations.CreateModel(
            name='WorksObjectProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nom')),
                ('input_type', models.CharField(choices=[('text', 'Texte'), ('checkbox', 'Case à cocher'), ('number', 'Nombre'), ('file', 'Fichier')], max_length=30, verbose_name='type de caractéristique')),
                ('is_mandatory', models.BooleanField(default=False, verbose_name='obligatoire')),
                ('works_object_types', models.ManyToManyField(related_name='properties', to='permits.WorksObjectType', verbose_name='objets des travaux')),
            ],
            options={
                'verbose_name': '1.5 Configuration du champ',
                'verbose_name_plural': '1.5 Configuration des champs',
            },
        ),
        migrations.AddField(
            model_name='worksobject',
            name='works_types',
            field=models.ManyToManyField(related_name='works_objects', through='permits.WorksObjectType', to='permits.WorksType', verbose_name='types'),
        ),
        migrations.CreateModel(
            name='PermitRequestGeoTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starts_at', models.DateTimeField(verbose_name='Date planifiée de début')),
                ('ends_at', models.DateTimeField(verbose_name='Date planifiée de fin')),
                ('comment', models.CharField(blank=True, max_length=1024, verbose_name='Commentaire')),
                ('external_link', models.URLField(blank=True, verbose_name='Lien externe')),
                ('geom', django.contrib.gis.db.models.fields.GeometryCollectionField(null=True, srid=2056, verbose_name='Localisation')),
                ('permit_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='geo_time', to='permits.PermitRequest')),
            ],
            options={
                'verbose_name': "3.3 Consultation de l'agenda et de la géométrie",
                'verbose_name_plural': '3.3 Consultation des agenda et géométries',
            },
        ),
        migrations.CreateModel(
            name='PermitRequestActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_type', models.PositiveSmallIntegerField(choices=[(0, 'Autres'), (2, 'Propriétaire'), (3, 'Entreprise'), (4, "Maître d'ouvrage"), (1, "Requérant si différent de l'auteur de la demande"), (5, 'Sécurité'), (6, 'Association')], default=0, verbose_name='type de contact')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permits.PermitActor')),
                ('permit_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permit_request_actors', to='permits.PermitRequest')),
            ],
            options={
                'verbose_name': 'Relation permis-contact',
                'verbose_name_plural': 'Relations permis-contact',
            },
        ),
        migrations.AddField(
            model_name='permitrequest',
            name='actors',
            field=models.ManyToManyField(related_name='_permitrequest_actors_+', through='permits.PermitRequestActor', to='permits.PermitActor'),
        ),
        migrations.AddField(
            model_name='permitrequest',
            name='administrative_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permit_requests', to='permits.PermitAdministrativeEntity', verbose_name='commune'),
        ),
        migrations.AddField(
            model_name='permitrequest',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='permit_requests', to='permits.PermitAuthor', verbose_name='auteur'),
        ),
        migrations.AddField(
            model_name='permitrequest',
            name='works_object_types',
            field=models.ManyToManyField(related_name='permit_requests', through='permits.WorksObjectTypeChoice', to='permits.WorksObjectType'),
        ),
        migrations.CreateModel(
            name='PermitActorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Autres'), (2, 'Propriétaire'), (3, 'Entreprise'), (4, "Maître d'ouvrage"), (1, "Requérant si différent de l'auteur de la demande"), (5, 'Sécurité'), (6, 'Association')], default=0, verbose_name='type de contact')),
                ('works_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works_contact_types', to='permits.WorksType', verbose_name='type de travaux')),
            ],
            options={
                'verbose_name': '1.6 Configuration du contact',
                'verbose_name_plural': '1.6 Configuration des contacts',
            },
        ),
        migrations.AlterUniqueTogether(
            name='worksobjecttype',
            unique_together={('works_type', 'works_object')},
        ),
        migrations.CreateModel(
            name='WorksObjectPropertyValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', django.contrib.postgres.fields.jsonb.JSONField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='permits.WorksObjectProperty', verbose_name='caractéristique')),
                ('works_object_type_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='permits.WorksObjectTypeChoice', verbose_name='objet des travaux')),
            ],
            options={
                'unique_together': {('property', 'works_object_type_choice')},
            },
        ),
        migrations.CreateModel(
            name='PermitRequestValidation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validation_status', models.IntegerField(choices=[(0, 'En attente'), (1, 'Approuvé'), (2, 'Refusé')], default=0, verbose_name='Statut de validation')),
                ('comment_before', models.TextField(blank=True, verbose_name='Commentaires (avant)')),
                ('comment_during', models.TextField(blank=True, verbose_name='Commentaires (pendant)')),
                ('comment_after', models.TextField(blank=True, verbose_name='Commentaires (après)')),
                ('validated_at', models.DateTimeField(null=True, verbose_name='Validé le')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permit_request_validations', to='permits.PermitDepartment')),
                ('permit_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='validations', to='permits.PermitRequest')),
                ('validated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '3.5 Consultation de la validation par le service',
                'verbose_name_plural': '3.5 Consultation des validations par les services',
                'unique_together': {('permit_request', 'department')},
            },
        ),
    ]
