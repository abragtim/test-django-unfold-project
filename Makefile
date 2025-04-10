# Update the repository
update:
	git fetch
	git pull

# Restart nginx
restart:
	sudo systemctl restart nginx

# Start Gunicorn with 9 workers
start:
	gunicorn --workers 9 test_django_project.wsgi:application

# Combined target to update repo, restart nginx, and start gunicorn
deploy: update restart start
