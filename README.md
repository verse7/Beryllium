# Beryllium
Mentee-Montor Programme Application


## REQUIREMENTS
see @rowatk or Lateefah

## Server

### Setting up virtual environment
To begin developing on the back end (flask) you must have python3.7 
#### installing python3.7 on Ubuntu 18.04 or debian based OS
> $ sudo apt install python3.7

#### using pipenv to setup virtual environment
> $ pip3 install pipenv
> $ cd server
> $ pipenv shell

Install all dependencies
> $ pipenv install --dev .

The `--dev .` specifies that the current directory is also to be installed as an editable package in the environment. This is done mainly to make imports easier. 
See [here](https://stackoverflow.com/a/50193944) for further explanation

If the error: "AttributeError: 'Marshmallow' object has no attribute 'ModelSchema'" occurs, the package marshmalow-sqlalchemy is needed.
to install:
> $ pipenv install marshmallow-sqlalchemy

#### deactivating virtual environment
> $ exit

see pipenv [docs](https://github.com/pypa/pipenv) for usage 

### Running the server
A python file - 'wsgi.py' acts as the driver to run the flask application. Execution of this file means execution of the flask server. Depending on your system the command to execute the file could be:
> $ python wsgi.py

> $ python3 wsgi.py

> $ python3.7 wsgi.py

### Understanding the server code
Some practices of using flask came from this tutorial series [here](https://hackersandslackers.com/configure-flask-applications). Some practices were omitted because they were unnecessary due to the current small scale of the app.

> NOTE: the creation of a `.env` file is necessary for the app configuration. An example (`.env.example`) is included for guidance. See [here](https://hackersandslackers.com/configure-flask-applications) also for further explanations.


## User Interface (UI)
The very little done right now uses the VueJs Framework. The framework of choice will most likely change therefore no instructions right now.

