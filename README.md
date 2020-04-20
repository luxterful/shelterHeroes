# Shelter Heroes Platform

A social media platform for shelters and their animals.

> ### Make a difference!
>
> There are thousands of animals living in shelters right now. You can be the difference in their lives. You can support our little four legged friends not only with an adoption, but also with a donation or simply by being their companion. Beyond that you can show off the cutest, funniest and quirkiest moments in the life of your own little furball to the world. Connect with the pet friends around you, arrange playdates, meet up for adventure. Be the difference.

## setup locally

#### 1. Create a virutal python 3 enviroment

    $ python3 -m venv env
    $ source /env/bin/activate

#### 2. To install dependencies in a local env:

    $ make install

#### 3. creates postgres database and add user

    $ createdb <dbname>

    $ psql <dbname>
    > CREATE ROLE <user> WITH LOGIN PASSWORD '<password>';

#### 4. set env variable for database URL

    $ export DATABASE_URL=postgresql://<user>:<password>@localhost:5432/<dbname>

#### 5. start the server

    $ make startserver

#### 6. To start the Client you need to open a new session an run

    $ make startclient
