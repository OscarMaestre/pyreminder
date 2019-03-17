#!/bin/bash
rm reminderapp/migrations/0*.py
rm reminderapp/migrations/0*.pyc
rm db.sqlite3
./manage.py makemigrations
./manage.py migrate
cat superuser.py | ./manage.py shell
./manage.py runserver
