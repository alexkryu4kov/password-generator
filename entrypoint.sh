#!/bin/bash

# Wait for the MySQL service
./wait-for-db.sh localhost 3306 --
flask db migrate
flask db upgrade

# Start the Flask app
gunicorn --workers=4 --bind=0.0.0.0:5000 run:app