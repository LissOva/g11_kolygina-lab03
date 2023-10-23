
from flask import Flask, request

app = Flask ('lab03')

@app.route('/test', methods=('GET','POST'))
def my_form():
	if request.method == "GET":
#	abc= request.args.get('param')
		abc= request.args.get('param')
	if request.method == "POST":
		abc= request.form.get('param')
	return 'Hello '+ abc + '!'
	
@app.route('/add', methods=('GET', 'POST'))
def my_add():
	a = request.args.get('a')
	b = request.args.get('b')
	sum = int(a) + int(b)
	ss= str(sum)
	return a + ' + ' + b + ' = ' + ss

