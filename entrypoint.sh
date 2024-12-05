#!/bin/bash
set -e

# Apply migrations and restore the database
echo "Applying database migrations..."
python manage.py migrate

echo "Restoring the database..."
python manage.py restore_db

# Start the Django development server
exec "$@"
