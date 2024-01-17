#!/bin/bash

source .env

# Wait for the MySQL service
./wait-for-db.sh ${MYSQL_HOST} 3306 --
flask db migrate
flask db upgrade

# Start the Flask app
gunicorn --workers=4 --bind=0.0.0.0:5000 run:app