# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
		abort, render_template, flash
from contextlib import closing

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development_key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our application
app = Flask(__name__)
app.config.from_object(__name__)

# connect to the application database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

# create a function to initialize the database
def init_db():
	# open a db connection
	with closing(connect_db()) as db:
		# open the schema file
		with app.open_resource('schema.sql', mode = 'r') as f:
			db.cursor().executescript(f.read())
		db.commit()

if __name__ == "__main__":
	app.run()
