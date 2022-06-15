# Overrides for development

version: "3"

volumes:
    pgdata:

services:
    web:
        # Runserver for live reload
        entrypoint: /code/entrypoint_demo.sh
        command: "python3 manage.py runserver 0.0.0.0:9000"
        volumes:
            # Mount code for live reload
            - .:/code
            # Local mount to debug QGIS projects
            - ./private_documents:/private_documents
        depends_on:
            - "postgres"
        ports:
            - "${DJANGO_DOCKER_PORT}:9000"
        environment:
            # Debug settings
            - DJANGO_SETTINGS_MODULE=geomapshark.settings_dev

    qgisserver:
        volumes:
            # Local mount to debug QGIS projects
            - ./private_documents:/private_documents #used to access to the private documents via a volume (check env.demo) search(ctrl+f) -> #access_to_private_document_local
        environment:
            - QGIS_SERVER_LOG_LEVEL=0

    postgres:
        image: postgis/postgis:13-3.2
        restart: unless-stopped
        environment:
            - POSTGRES_USER=${PGUSER}
            - POSTGRES_PASSWORD=${PGPASSWORD}
            - POSTGRES_DB=${PGDATABASE}
        ports:
            - "${POSTGRES_DOCKER_PORT}:5432"
        volumes:
            - pgdata:/var/lib/postgresql/data

    mailhog:
        container_name: mailhog
        tty: true
        image: mailhog/mailhog
        logging:
            driver: 'none'  # disable saving logs
        ports:
            - 1025:1025 # smtp server
            - 8025:8025 # web ui
