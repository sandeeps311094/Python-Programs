#---  A very basic Flask Application


import os
from flask import Flask, render_template

app = Flask(__name__) 

@app.route ("/")
@app.route("/home")
def home():
	#return "<h1> Flask_Webdriver_27 !</h1>"
	return render_template('home.html')


@app.route ("/")
@app.route("/about")
def about():
	#return "<h1> About ! </h1>"
	return render_template('about.html')

# - - - -

if __name__ == '__main__':
	app.run(debug = True)
