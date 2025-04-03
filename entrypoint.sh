#!/usr/bin/env sh


echo "TARGET_CONTAINER: $TARGET_CONTAINER"

if [ "$TARGET_CONTAINER" = "ude_jose" ]; then
	# Collect static files
	# python manage.py collectstatic --noinput

	# Apply migrations (if needed)
	python manage.py migrate

	# Start Gunicorn
	# gunicorn _prj.wsgi:application --bind 0.0.0.0:8000
    python manage.py runserver 0.0.0.0:8000
fi

# Default command or pass-through for other containers
exec "$@"