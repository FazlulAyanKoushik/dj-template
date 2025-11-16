#!/bin/sh

echo "Starting Django application..."

# shellcheck disable=SC2164
cd /app/core

# Load DB type from environment
if [ "$DATABASE_TYPE" = "postgres" ]; then
    echo "Waiting for PostgreSQL at $DB_HOST:$DB_PORT..."

    while ! nc -z "$DB_HOST" "$DB_PORT"; do
        sleep 0.5
    done

    echo "PostgreSQL is available."
else
    echo "Using SQLite. Skipping database availability check."
fi

# Run migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Seed initial users
echo "Seeding initial users..."
python manage.py seed_users || echo "User seeding skipped (user may already exist)"

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear || echo "Static files collection failed, continuing..."

# Run the main container command (e.g., gunicorn / daphne / runserver)
exec "$@"

