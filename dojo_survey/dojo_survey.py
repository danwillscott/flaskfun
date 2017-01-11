from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
          # The "@" symbol designates a "decorator" which attaches the following # function to the '/' route. This means that whenever we send a request to
app.secret_key = "SKEY12345"                     
                      
@app.route('/')
def index():		# localhost:5000/ for index.html
	return render_template('index.html')
	
@app.route('/result') #	# localhost:5000/result is the location of the result ******* This is where you redirect to when you post the infomation by submitting 
def result():
	return render_template('result.html')  


# In here i will do a request.form

# the function goes here that handles the data

@app.route('/', methods=['Post'])
def routeData():
	userName = request.form['fullname']
	userLoc = request.form['loc']
	userFav = request.form['lang']
	userComment = request.form['comment']
	return render_template('result.html', name=userName, loc=userLoc, lang=userFav, comment=userComment)

app.run(debug=True)      # Run the app in debug mode if debug is set to True.
