#!/bin/sh

# Wait for Postgres to become available
until PGPASSWORD="$POSTGRES_PASSWORD" psql -h db -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
    sleep 1
done

# Cambia al directorio de alembic y ejecuta las migraciones
cd /app/applications/sip_application/migrations
alembic upgrade head

# Cambia al directorio de web2py e inicia la aplicación
cd /app
exec python web2py.py -a 'root' -c cert.pem -k key.pem -i 0.0.0.0
