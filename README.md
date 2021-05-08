# ENHANCE AUTOMATION OF THE ACADEMIC TIMETABLE

The timetable is one of the essential things in any educational institute. Because if the timetable was made perfectly it will help everyone either it’s a student, instructor, and an administration member in having a good semester free of failure.

And creating the timetable is a complex task that takes so much time, so we made it easier with this web app, you can create timetables with a click of a button.

Hosted Link: https://qassim-university-timetable.herokuapp.com/

While running locally: http://localhost:5000


## Getting Started

### Installing Dependencies


#### Python

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).


#### PostgreSQL

Follow instructions to install the latest version of PostgreSQL for your platform in the [PostgreSQL docs](https://www.postgresql.org/download/).


#### PIP Dependencies

Install the dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages.


##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight database. You'll primarily work in app.py, models.py, and database_oparations. 



### Setting up the Database


#### Link the Database

To link the app to the database go to the file `models.py` and paste the link of your database in the right place, you will find it in the bottom of the file like this:

```
engine = create_engine('postgresql://username:password@localhost:port/database_name', echo=True)
```

You can either change the variables in the code with your own, or paste the link of your database inside the single quotation marks.


#### Import the mock data database

The backup file `data.sql` in the directory, it contains the scheme and mock data for the CS department with all the necessary data like courses, instructors, student plan, ...etc.

To import the backup file to your database, run the following command:

```bash
psql -U username dbname < data.sql
```

With this you will have all the data you need to experiment with the app.


## Running the server

To run the server, execute:

```bash
export FLASK_APP=main.py
flask run --reload
```

Setting the `FLASK_APP` variable to `main.py` directs flask to use the `mian.py` file to find the application. 

Using the `--reload` flag will detect file changes and restart the server automatically.

Or another way to run the server is to double click on the `main.py` and the server will run.
