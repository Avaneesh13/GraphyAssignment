web: gunicorn GraphyAssignment.wsgi --log-file -
worker: celery -A stories.tasks worker -B --loglevel=info