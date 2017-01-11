from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app.
import random
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
          # The "@" symbol designates a "decorator" which attaches the following # function to the '/' route. This means that whenever we send a request to
app.secret_key = "SKEY12345"                     
    


def thisSessionCounter(num):
	if num == 0:
		try:
			session['counter'] += 1
			return session['counter']
		except KeyError:
			session['counter'] = 1
			return session['counter']
	if num == 1:
		session['counter'] = -1
		return session['counter']
	if num == 2:
		session['counter'] += 1
		return session['counter']
	
def randomControler(aBool):
	if aBool:
		try:
			session['ranKey']

		except KeyError:
			session['ranKey'] = random.randrange(0, 101)
			return session['ranKey']
	else:
		session.pop('ranKey')

@app.route('/')
def index():		# localhost:5000/ for index.html
	count = thisSessionCounter(0)
	return render_template('index.html', count=count)


# In here i will do a request.form

# the function goes here that handles the data

@app.route('/', methods=['Post'])
def routeData():
	aValue = request.form['postdata']
	print aValue
	if aValue == "reset":
		thisSessionCounter(1)
		return redirect('/')
	elif aValue == "plus2":
		thisSessionCounter(2)
		return redirect('/')



app.run(debug=True)      # Run the app in debug mode if debug is set to True.
