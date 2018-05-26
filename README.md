# Blog

## Installation

Make sure you have installed in your OS
```
make
python3.6
virtualenv
postgresql
```

Create a PostgreSQL database
```sh
sudo su - postgres
psql
CREATE DATABASE blog;
CREATE USER blog WITH PASSWORD 'blog';
GRANT ALL PRIVILEGES ON DATABASE blog TO blog;
ALTER USER blog CREATEDB;
```

Then run:
```
make requirements
make virtualenv_test
source venv/bin/activate
cd src/
./manage migrate
```

## Run tests

Run `make tests`. It will do isort-check, lint and django tests.

## Utils

Update packages: `make requirements`. Creates a requirements.txt file with the last versions of the packages inside requirements/base.txt. You can run it whenever you want to update your project. It will create a temporary virtualenv.

`make virtualenv` Creates a new virtualenv using requirements.txt.

`make virtualenv_test` Creates a development virtualenv using requirements.txt and packages from requirements/test.txt.

`make clean` Removes the .pyc files and deletes the virtualenv folder.

`make isort` Checks your code and fixes the imports using isort.

## Template theme

https://github.com/BlackrockDigital/startbootstrap-clean-blog
