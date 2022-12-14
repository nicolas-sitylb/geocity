# Variables to change the result of the seeder

# Defines the number of each type of user to create on each entity
iterations = {
    "integrator_iterations": 3,
    "pilot_iterations": 5,
    "validator_iterations": 6,
    "user_iterations": 8,
}

# domain:entity
# Users created (password demo) :
#   - ENTITY-superuser
#   - ENTITY-integrator-ITERATION
#   - ENTITY-pilot-ITERATION
#   - ENTITY-validator-ITERATION
#   - ENTITY-user-ITERATION
entities = {
    "first.ch": "first_entity",
    "second.ch": "second_entity",
    "third.ch": "third_entity",
    "fourth.ch": "fourth_entity",
    "fifth.ch": "fifth_entity",
}

# Geometries for the entities
geoms = [
    "SRID=2056;MultiPolygon (((2538391 1176432, 2538027 1178201, 2538485 1178804, 2537777 1179199, 2536748 1178450, 2536123 1179647, 2537382 1180593, 2537143 1181623, 2538651 1183257, 2540368 1183236, 2541252 1181093, 2541460 1180458, 2540160 1179543, 2540097 1178877, 2538391 1176432)))",
    "SRID=2056;MultiPolygon (((2543281 1184952, 2542053 1186731, 2541148 1186887, 2538214 1186367, 2537195 1184609, 2537153 1183330, 2537757 1182653, 2539317 1182404, 2543281 1184952)))",
    "SRID=2056;MultiPolygon (((2533045 1151566, 2533789 1154840, 2538236 1155380, 2541064 1154989, 2541790 1157408, 2540934 1160087, 2543074 1161259, 2546553 1159715, 2545399 1156329, 2542757 1155361, 2542348 1153798, 2542497 1152347, 2540692 1150617, 2535855 1152105, 2533045 1151566)),((2529938 1157110, 2529789 1160329, 2532245 1161557, 2532580 1160273, 2530831 1158934, 2530757 1157259, 2529938 1157110)))",
    "SRID=2056;MultiPolygon (((2553381 1146430, 2553679 1145798, 2553660 1145500, 2554777 1145296, 2555502 1145965, 2554870 1146617, 2555335 1147398, 2555037 1147417, 2554311 1146803, 2553418 1146840, 2553269 1146524, 2553381 1146430)))",
    "SRID=2056;MultiPolygon (((2538391 1176432, 2538027 1178201, 2538485 1178804, 2537777 1179199, 2536748 1178450, 2536123 1179647, 2537382 1180593, 2537143 1181623, 2538651 1183257, 2540368 1183236, 2541252 1181093, 2541460 1180458, 2540160 1179543, 2540097 1178877, 2538391 1176432)))",
]

# Ofs_ids for the entities
ofs_ids = [5938, 5938, 5586, 5890, 5938]

# Define the fields
field_comment = {
    "name": "Commentaire",
    "input_type": "text",
    "is_mandatory": False,
}
field_width = {
    "name": "Largeur [m]",
    "input_type": "number",
    "placeholder": "3",
    "help_text": "Largeur en mètres",
    "is_mandatory": False,
}
field_title = {
    "name": "Texte permettant de séparer visuellement les champs",
    "input_type": "title",
    "help_text": "Ce texte permet d'expliquer en détail à l'utilisateur les pourquoi et le comment des informations à fournir",
    "is_mandatory": False,
}
field_height = {
    "name": "Hauteur [m]",
    "input_type": "number",
    "placeholder": "2",
    "help_text": "Longueur en mètres",
    "is_mandatory": False,
}
field_plan = {
    "name": "Plan de situation",
    "input_type": "file",
    "help_text": "Plan complémentaire détaillant votre projet",
    "is_mandatory": False,
}
field_adresse = {
    "name": "Adresse",
    "input_type": "address",
    "placeholder": "Place Pestalozzi 2, 1400 Yverdon-les-Bains",
    "is_mandatory": False,
}
field_adresse_geocode = {
    "name": "Adresse avec géocodage",
    "input_type": "address",
    "placeholder": "Place Pestalozzi 2, 1400 Yverdon-les-Bains",
    "is_mandatory": False,
    "store_geometry_for_address_field": True,
}
field_date = {
    "name": "Date",
    "input_type": "date",
    "is_mandatory": False,
}
field_checkbox = {
    "name": "Impact sur la chaussée",
    "input_type": "checkbox",
    "is_mandatory": False,
}
field_list_single = {
    "name": "À moins de 3m d'un arbre",
    "input_type": "list_single",
    "is_mandatory": False,
    "choices": "oui\nnon",
}
field_list_multiple = {
    "name": "À moins de 3m d'un arbre",
    "input_type": "list_multiple",
    "is_mandatory": False,
    "choices": "Déviation trafic\nHoraire prolongé\nSon>90dB",
}

# Define form_categories for each entity
form_categories = [
    (
        "Stationnement (ex. de demande devant être prolongée)",
        [
            (
                "Demande de macaron",
                field_comment,
                field_date,
            ),
            (
                "Accès au centre-ville historique",
                field_plan,
                field_width,
                field_comment,
                field_title,
                field_date,
                field_checkbox,
                field_adresse,
                field_list_multiple,
            ),
        ],
    ),
    (
        "Événements sur la voie publique",
        [
            (
                "Événement sportif",
                field_plan,
                field_width,
                field_comment,
                field_title,
                field_date,
                field_checkbox,
                field_adresse,
                field_list_multiple,
            ),
            (
                "Événement culturel",
                field_plan,
                field_width,
                field_comment,
                field_title,
                field_date,
                field_checkbox,
                field_adresse,
                field_list_multiple,
            ),
            (
                "Événement politique",
                field_plan,
                field_width,
                field_comment,
                field_title,
                field_date,
                field_checkbox,
                field_adresse,
                field_list_multiple,
            ),
            (
                "Événement commercial",
                field_plan,
                field_width,
                field_comment,
                field_title,
                field_date,
                field_checkbox,
                field_adresse,
                field_list_multiple,
            ),
        ],
    ),
    (
        "Chantier",
        [
            (
                "Permis de fouille",
                field_width,
                field_height,
                field_title,
                field_comment,
                field_adresse,
                field_adresse_geocode,
                field_checkbox,
                field_list_single,
            ),
            (
                "Permis de dépôt",
                field_width,
                field_height,
                field_comment,
                field_title,
                field_adresse,
                field_adresse_geocode,
                field_checkbox,
            ),
        ],
    ),
    (
        "Subventions (ex. de demande sans géométrie ni période temporelle)",
        [
            (
                "Prime éco-mobilité",
                field_comment,
            ),
            (
                "Abonnement de bus",
                field_comment,
            ),
        ],
    ),
]

form_additional_information = """
Texte expliquant la ou les conditions particulière(s) s'appliquant à cette demande.
Un document pdf peut également être proposé à l'utilisateur, par exemple pour les conditions
de remise en état après une fouille sur le domaine public
"""


# Store all fields to apply
# fields = [
#     field_comment,
#     field_width,
#     field_title,
#     field_height,
#     field_plan,
#     field_adresse,
#     field_adresse_geocode,
#     field_date,
#     field_checkbox,
#     field_list_single,
#     field_list_multiple,
# ]

# form_categories = {
#     "Stationnement (ex. de demande devant être prolongée)":[
#         [
#             "Demande de macaron", "comment", "date"
#         ],
#         [
#             "Accès au centre-ville historique", "plan", "width", "comment", "title", "date", "checkbox", "adresse", "list_multiple"
#         ]
#     ],
#     "Événements sur la voie publique":[
#         [
#             "Événement sportif", "plan", "width", "comment", "title", "date", "checkbox", "adresse", "list_multiple",
#         ],
#         [
#             "Événement culturel", "plan", "width", "comment", "title", "date", "checkbox", "adresse", "list_multiple",
#         ],
#         [
#             "Événement politique", "plan", "width", "comment", "title", "date", "checkbox", "adresse", "list_multiple",
#         ],
#         [
#             "Événement commercial", "plan", "width", "comment", "title", "date", "checkbox", "adresse", "list_multiple",
#         ],
#     ],
#     "Chantier":[
#         [
#             "Permis de fouille", "width", "height", "title", "comment", "adresse", "adresse_geocode", "checkbox", "list_single",
#         ],
#         [
#             "Permis de dépôt", "width", "height", "comment", "title", "adresse", "adresse_geocode", "checkbox",
#         ],
#     ],
#     "Subventions (ex. de demande sans géométrie ni période temporelle)":[
#         [
#             "Prime éco-mobilité", "comment",
#         ],
#         [
#             "Abonnement de bus", "comment",
#         ],
#     ]
# }

# Define fields for each entity
# fields = {
#     "comment": Field.objects.create(
#         name="Commentaire",
#         input_type="text",
#         is_mandatory=False,
#     ),
#     "width": Field.objects.create(
#         name="Largeur [m]",
#         input_type="number",
#         placeholder="3",
#         help_text="Largeur en mètres",
#         is_mandatory=False,
#     ),
#     "title": Field.objects.create(
#         name="Texte permettant de séparer visuellement les champs",
#         input_type="title",
#         help_text="Ce texte permet d'expliquer en détail à l'utilisateur les pourquoi et le comment des informations à fournir",
#         is_mandatory=False,
#     ),
#     "height": Field.objects.create(
#         name="Hauteur [m]",
#         input_type="number",
#         placeholder="2",
#         help_text="Longueur en mètres",
#         is_mandatory=False,
#     ),
#     "plan": Field.objects.create(
#         name="Plan de situation",
#         input_type="file",
#         help_text="Plan complémentaire détaillant votre projet",
#         is_mandatory=False,
#     ),
#     "adresse": Field.objects.create(
#         name="Adresse",
#         input_type="address",
#         placeholder="Place Pestalozzi 2, 1400 Yverdon-les-Bains",
#         is_mandatory=False,
#     ),
#     "adresse_geocode": Field.objects.create(
#         name="Adresse avec géocodage",
#         input_type="address",
#         placeholder="Place Pestalozzi 2, 1400 Yverdon-les-Bains",
#         is_mandatory=False,
#         store_geometry_for_address_field=True,
#     ),
#     "date": Field.objects.create(
#         name="Date",
#         input_type="date",
#         is_mandatory=False,
#     ),
#     "checkbox": Field.objects.create(
#         name="Impact sur la chaussée",
#         input_type="checkbox",
#         is_mandatory=False,
#     ),
#     "list_single": Field.objects.create(
#         name="À moins de 3m d'un arbre",
#         input_type="list_single",
#         is_mandatory=False,
#         choices="oui\nnon",
#     ),
#     "list_multiple": Field.objects.create(
#         name="À moins de 3m d'un arbre",
#         input_type="list_multiple",
#         is_mandatory=False,
#         choices="Déviation trafic\nHoraire prolongé\nSon>90dB",
#     ),
# }

# # Define form_categories for each entity
# form_categories = [
#     (
#         "Stationnement (ex. de demande devant être prolongée)",
#         [
#             (
#                 "Demande de macaron",
#                 fields["comment"],
#                 fields["date"],
#             ),
#             (
#                 "Accès au centre-ville historique",
#                 fields["plan"],
#                 fields["width"],
#                 fields["comment"],
#                 fields["title"],
#                 fields["date"],
#                 fields["checkbox"],
#                 fields["adresse"],
#                 fields["list_multiple"],
#             ),
#         ],
#     ),
#     (
#         "Événements sur la voie publique",
#         [
#             (
#                 "Événement sportif",
#                 fields["plan"],
#                 fields["width"],
#                 fields["comment"],
#                 fields["title"],
#                 fields["date"],
#                 fields["checkbox"],
#                 fields["adresse"],
#                 fields["list_multiple"],
#             ),
#             (
#                 "Événement culturel",
#                 fields["plan"],
#                 fields["width"],
#                 fields["comment"],
#                 fields["title"],
#                 fields["date"],
#                 fields["checkbox"],
#                 fields["adresse"],
#                 fields["list_multiple"],
#             ),
#             (
#                 "Événement politique",
#                 fields["plan"],
#                 fields["width"],
#                 fields["comment"],
#                 fields["title"],
#                 fields["date"],
#                 fields["checkbox"],
#                 fields["adresse"],
#                 fields["list_multiple"],
#             ),
#             (
#                 "Événement commercial",
#                 fields["plan"],
#                 fields["width"],
#                 fields["comment"],
#                 fields["title"],
#                 fields["date"],
#                 fields["checkbox"],
#                 fields["adresse"],
#                 fields["list_multiple"],
#             ),
#         ],
#     ),
#     (
#         "Chantier",
#         [
#             (
#                 "Permis de fouille",
#                 fields["width"],
#                 fields["height"],
#                 fields["title"],
#                 fields["comment"],
#                 fields["adresse"],
#                 fields["adresse_geocode"],
#                 fields["checkbox"],
#                 fields["list_single"],
#             ),
#             (
#                 "Permis de dépôt",
#                 fields["width"],
#                 fields["height"],
#                 fields["comment"],
#                 fields["title"],
#                 fields["adresse"],
#                 fields["adresse_geocode"],
#                 fields["checkbox"],
#             ),
#         ],
#     ),
#     (
#         "Subventions (ex. de demande sans géométrie ni période temporelle)",
#         [
#             (
#                 "Prime éco-mobilité",
#                 fields["comment"],
#             ),
#             (
#                 "Abonnement de bus",
#                 fields["comment"],
#             ),
#         ],
#     ),
# ]
