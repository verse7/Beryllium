# Beryllium
Mentee-Montor Programme Application


## REQUIREMENTS - to be changed
- Randomly assign mentees to *free* mentors
1)free = mentor with number of mentee < max
2)max is defined by data (not constant for all mentors)

- View all mentors
- View mentees for a specific mentor
- View all free mentors
- Vew view all free mentees

## Back End

### Setting up virtual environment
To begin developing on the back end (flask) you must have python3.7 
#### installing python3.7 on Ubuntu 18.04 
> sudo apt install python3.7 on debian-based linux

#### using pipenv to setup virtual environment
> pip3 install pipenv
> pipenv shell
> pipenv install

If the error: "AttributeError: 'Marshmallow' object has no attribute 'ModelSchema'" occurs, the package marshmalow-sqlalchemy is needed.
to install:
> pipenv install marshmalow-sqlalchemy

see pipenv [docs](https://github.com/pypa/pipenv) for usage 

### Running the server
A python file - 'run.py' acts as the driver to run the flask application. Execution of this file means execution of the flask server. Depending on your system the command to execute the file could be:
> python run.py

> python3 run.py

> python3.7 run.py
