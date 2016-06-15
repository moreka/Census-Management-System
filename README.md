# Census Management System
A system for managing and searching the data released by Word Bank.

## Setup
You must install required packages using pip:
`pip install -r requirments.txt`

Then you must go to `census/static` and run bower to install UI packages:

`bower install`

If you don't have bower installed, you should install it with npm:

`npm install -g bower`

After theses steps, with running `python3 manage.py migrate`, you should instantiate all needed tables in the database.

Finally, with `python3 manage.py runserver`, the webserver is up and you can see the website by pointing your browser to `localhost:8000`.

## Important urls
`/import`: imports data from data files
`/login`: logins to system
`/logout`: logs out from system
`/`: index page, which show the required tables

Have fun!
