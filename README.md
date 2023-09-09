# How to install

0. Go to folder TankSite/main
1. python -m venv ../venv
2. pip install -r .\requirements.txt
3. python manage.py makemigrations firstapp
4. python manage.py migrate
5. python manage.py runserver

----

pip install
pip freeze > requirements.txt