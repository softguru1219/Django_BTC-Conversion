### install django
```
virtualenv venv -p python3
source teste/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


### TODO


* Create simple comand in manage.py for check every 5 min if exist new payment for orders created in last 24 hours. for add in crontab.

* Add simple comand in manage.py `autoconfig` and automatic create profiles for Crypto Currency.
----




### SETUP

```
gem install heroku
heroku create
git push heroku master
heroku run python manage.py migrate
heroku run python manage.py loaddata exchange/fixtures/initial.json
heroku run python manage.py loaddata exchange/fixtures/initial.json --exclude auth.permission --exclude contenttypes
heroku run python manage.py runserver
```
