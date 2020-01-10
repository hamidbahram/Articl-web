# Article-web
# try-django-2.2.6
- [Visit the site](http://hamidbahram.pythonanywhere.com/articles/)


installation
--------------------
- requirements:
 - python 3.7
  install following packages via **pip** or **easy_install**
- `pip install Django==2.2.6`
- `pip install djangorestframework==3.5.2`
- `pip install django-filter==1.0.1`
- `pip install django-ckeditor==5.8.0`
- `pip install django-js-asset==1.2.2`
- `pip install idna==2.8`
- `pip install Pillow==6.2.0`
- `pip install python-dateutil==1.5`
- `pip install pytz==2019.2`
- `pip install requests==2.22.0`
- `pip install sqlparse==0.3.0`
- `pip install urllib3==1.25.6`
- create database by typing `python manage.py migrate`
- run your server by typing `python manage.py runserver`

> **Note:**

> - You need to create an admin user to manage your blog site by this command: `python manage.py createsuperuser`

Create url: open teminal and type this url. Note that httpie must be installed.

`$ http -a <USERNAME>:<PASSWORD> http://127.0.0.1:8000/api/create/ title='<YOUR_TITLE>' slug='<YOUR_SLUG>' body='YOUR_BODY' owner=<OWNER_ID>`

Delete url: open teminal and type this url.

`$ http -a <USERNAME>:<PASSWORD> DELETE http://127.0.0.1:8000/api/<POST_ID / POST_SLUG >/delete`

Update url: open teminal and type this url.

`$ http -a <USERNAME>:<PASSWORD> PUT http://127.0.0.1:8000/api/<POST_ID / POST_SLUG >/edit title='<YOUR_TITLE>' content='<YOUR_CONTENT>' owner=<OWNER_ID>`

> **Note:**

> - Django Server Error: port is already in use: 
> - A more simple solution just type `sudo fuser -k 8000/tcp`. This should kill all the processes associated with port 8000.
> **EDIT:**
> - For osx users you can use `sudo lsof -t -i tcp:8000 | xargs kill -9`.

#### Follow me
- [Email](https://hamidbahram2@gmail.com)
- [Github](https://github.com/hamidbahram)
- [Telegram](https://telegram.me/hamiid_bh)
- [Instagram](https://www.instagram.com/_hamiid_bh/)
