## flask-cron-docker
Docker container with Flask web server and cron in background.

To start the docker, run `docker-compose up`. The web server will then start up, with cron running in the background.
Two crontab examples are already populated in `/cron_data/crontab`. The first runs a command line echo, while the second runs an example Python script.

Docker healthcheck checks that the background cron daemon is active. Crontabs are re-read at container start-up.
