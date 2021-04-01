# Alfax

this is the first Version of Alfax made by Love in Django.


## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ git clone git@gitlab.com:jupidev-code/alfax.ir.git
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt

# Create Super user And Migrations.

$ cd alfax.ir/
$ python manage.py createsuperuser 
$ python manage.py makemigrations
$ python manage.py migrate

# Finally Run Project.

$ python manage.py runserver <port>

```
## Installation  With  Docker

Run Project on Docker

#### 1. install Docker And Docker-compose on your system 

For Ubunto
```bash
$ sudo apt install docker.io
$ sudo apt install docker-compose
```
#### 2. Create Volumes And Networks on your System

Create volumes
```bash
$ sudo docker volume create alfax_static_volume
$ sudo docker volume create alfax_media_volume
$ sudo docker volume create alfax_postgresql

```
Create Networks
```bash
$ sudo docker network create alfax_network
$ sudo docker network create nginx_network
```
Run docker-composers 

```bash
$ git clone git@gitlab.com:jupidev-code/alfax.ir.git
$ cd Alfax/ 
$ sudo docker-compose up -d
$ cd config/nginx
$ sudo docker-compose up -d

```

Enjoy it :)

## Features

* Manage and Modify your Company Contact.
* Manage and Modify your Company Accounting.
* Manage and Modify Construction Company Accounting.
* Split settings in two files. `settings_custom.py` for specific environment settings (localhost, production, etc). `projectname/settings.py` for core settings.
* Simple logging setup ready for production envs.

## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.


## TODO List
    [✔] set up Jalali Calender for Project
    [✔] Look up for Blog and Landing Page Template and Add To Project
    [✔] change Admin page Front End
    [ ] Add item 'Add Contact' to Contact 
    [ ] mail verifacation
    [ ] sms verifecation
    [ ] Project page show All project


    [✔] Add Landing Page Models
    [✔] Add Resume Page Models

    [ ] Set Up Resume Page Html With View
    [✔] Set up New Landing Page 
    [✔] Set up project detail Page 
    [ ] set Up menu links in html pages

    [✔] Add Model Managers to Blog
    [✔] Add Model Managers to Land(prject)
    [ ] Add Model Menu Links in header to Land

    [✔] add a project as a new application
    [✔] add a Landing as a new application
    [✔] add a Dashboard as a new application
    [✔] add a blog as a new application
    [ ] add Contact as new application in dashboard
    [✔] add karfarmaonline as a new application in dashboard
    [ ] add Elevator app as new application in dashboard