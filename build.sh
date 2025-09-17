#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

# Reset migrations pour éviter les conflits
python manage.py migrate --fake apx_app zero
python manage.py migrate apx_app 0001 --fake
python manage.py migrate