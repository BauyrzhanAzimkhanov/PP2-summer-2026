#!/bin/bash

apt update
apt install postgresql libpq-dev gcc

python3 -m venv venv

source venv/bin/activate

# deactivate

pip install psycopg2

pip freeze > requirements.txt