# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template
import os

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

print(os.listdir())

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/elements')
def aboutUs():
	return render_template("elements.html")

@app.route('/events')
def events():
	return render_template("events.html")

@app.route('/events-news')
def gallery():
	return render_template("events-news.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/singleEvent')
def singleEvent():
	return render_template("single-event10.html")
@app.route('/index1')
def index1():
	return render_template("index1.html")



# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run()
