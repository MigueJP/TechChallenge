from flask import Flask, render_template, request

webapp = Flask(__name__)

@webapp.route('/', methods = ['GET', 'POST'])
def index():
	msg = ''
	if request.method == 'POST':
		msg = 'Hello from James!'
	return render_template('index.html', message = msg)