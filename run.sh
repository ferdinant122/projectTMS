#!/bin/sh

docker stop flask_app_c1

docker rm flask_app_c1

docker run -d -p 4449:5000 --name flask_app_c1 flask_app:v1.0
