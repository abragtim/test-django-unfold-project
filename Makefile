# Update the repository
update:
	git fetch
	git pull

# Restart nginx
restart-nginx:
	sudo systemctl restart nginx

start:
	@echo "Starting Gunicorn with 5 workers..."
	@nohup gunicorn --workers 5 test_django_project.wsgi:application > gunicorn.log 2>&1 &

stop:
	@echo "Stopping Gunicorn..."
	@PID=$$(ps aux | grep 'gunicorn' | grep -v 'grep' | awk '{print $$2}'); \
	if [ -n "$$PID" ]; then kill $$PID; else echo "No Gunicorn process found."; fi

# Combined target to update repo, restart nginx, and start gunicorn
deploy: update restart-nginx stop start
