del reminderapp\migrations\0*.py
del reminderapp\migrations\0*.pyc
del db.sqlite3
manage.py makemigrations
manage.py migrate
type superuser.py | manage.py shell
manage.py runserver