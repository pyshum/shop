How to install (for Linux).

apt install python3

pip3 install virtualenv

mkdir django-shop

cd django-shop

virtualenv env

source env/bin/activate

git clone git@github.com:pyshum/shop.git

cd /shop

pip install -r requirements.txt

python manage.py runserver

Go to the http://127.0.0.1:8000 in browser to see the website.
