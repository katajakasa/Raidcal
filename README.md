# Raidcal

RaidCal is a really simple raid calendar for MMO's such as WoW and GW2. It allows scheduling events and lets
users join them. Events get locked an hour before the event starts.

## 1. Requirements

* Python 2.7 and pip
* bower (depends on node.js and npm)
* For python deps, please see ```requirements.txt```.
* For JS deps, please see ```bower.json```.
* A database. A proper database like PostgreSQL or MySQL is recommended. Sqlite is not tested, but may work.

## 2. Installation for development

1. CD to your virtualenv directory, set up a virtualenv and activate it: ```virtualenv raidcal && source raidcal/bin/activate```. 
2. CD to your website directory and extract the archive or ```git clone https://github.com/katajakasa/Raidcal.git raidcal```.
3. Copy raidcal/settings.py-dist to raidcal/settings.py, and edit as necessary.
4. Install JS requirements:```bower install```.
5. Install python requirements: ```pip install -r requirements.txt```.
6. Run database migrations: ```python manage.py migrate```.
7. Create a superuser: ```python manage.py createsuperuser```.
8. Run the testing server: ```python manage.py runserver 0.0.0.0 8000```. Switch bind ip and port as necessary.

## 3. Installation for production

This depends very much on your setup, and therefore there's no quick quide for this. I recommend using eg. nginx
as a frontend to serve the static files, and uwsgi to run the django as a process. Uwsgi-emperor or supervisord can be
used to start and stop processes as required / at boot.

### 3.1. Sample production update/deployment script

Here's a really simple script for updating a production deployment. It's rather simplified and trusts
that the user rights etc. are correct, but it works fine as an example.

```
#!/bin/bash

source /var/virtualenv/raidcal/bin/activate
cd /var/www/raidcal/
git pull
pip install --upgrade -r requirements.txt
bower install
python manage.py migrate
python manage.py compress
python manage.py collectstatic --noinput
python manage.py compilemessages
sudo service uwsgi reload
```

### 3.2. Sample production nginx config

* upstream defines the port and location where nginx can find your wsgi-process.
* Location /static: This directory contains the static files (css, js, images ...) of the raidcal project. Serve this via nginx.
* Location /: Proxy this stuff to the wsgi process

```
upstream upstream-raidcal {
    server 127.0.0.1:9001;
}

server {
    listen 80;
    server_name mysite.com www.mysite.com;
    access_log /var/log/nginx/raidcal.log;
    error_log /var/log/nginx/raidcal.log;
    location /static {
        root /var/www/raidcal/content/;
    }
    location / {
        uwsgi_pass upstream-raidcal;
        include /etc/nginx/uwsgi_params;
    }
}
```

### 3.3. Sample production uwsgi-emperor config

* Make sure the socket is the same as in nginx configuration.
* Home should point at the virtualenv

```
[uwsgi]
chdir           = /var/www/raidcal
wsgi-file       = /var/www/raidcal/raidcal/wsgi.py
home            = /var/virtualenv/raidcal
master          = true
processes       = 5
socket          = :9001
vacuum          = true
daemonize       = /var/log/uwsgi/app/raidcal.log
plugin          = python
uid             = www-data
gid             = www-data
```

## 4. License

MIT. See ```LICENSE``` for details.
