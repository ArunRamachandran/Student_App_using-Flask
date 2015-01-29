from flask import render_template, flash, redirect, url_for, session
from flask import request
import sqlite3 as lite
import os
from functools import wraps
from app import app
from .forms import LoginForm
from wtforms.validators import Required
#from flask.ext.wtf import form
import sys

'''def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first !')
			return redirect(url_for('login'))
	return wrap'''


#form = LoginForm()

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
#	form = LoginForm(csrf_enabled=True)
	
#	if form.validate_on_submit():
#		flash('Login requested fot openid="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
#		return redirect('/fail')

#	if form.validate():
#		error = error
	
	return render_template('login_new.html', title='LogIn')


@app.route('/fail')
def fail():
	return '''
	<html>
		<head>
		<title>Home Page</title>
		</head>
		<center>
		<body>
			<h2>Provide Valid Information !</h2>
			<p><a href="home.html">Go Back</a></p>
		</body>
	</html> '''
		
@app.route('/index')
#@login_required
def index():
	#if request.method == 'POST':
	#	openid = request.form.get('openid')
	#if openid == None:
	#return render_template('/login', title="Log In")
	return render_template('home.html', title='Home')



@app.route('/about')
def about():
	return render_template('about.html', title='About')



@app.route('/insert', methods = ['GET', 'POST'])
def insert():
	userid = request.form['userid']
	if userid == '':
		return redirect('/login')
	return render_template("insert_form.html", title="Input")



@app.route('/process', methods=['GET', 'POST'])
def process():
	sname = request.form['sname']
	mark  = request.form['mark']
	
	if sname == '' or mark == '':
		return redirect('/fail')
	
	#if sname or mark == None:
	#	return redirect('/insert')
	con = lite.connect('student.db')
	
	with con:
		cur = con.cursor()
		cur.execute('insert into student(sname, mark) values(?,?)',[sname,mark])
	flash('Database Succesfully Updated !')
	return render_template('final.html', title="Updated")



@app.route('/view', methods=['GET', 'POST'])
def view():
	
	con = lite.connect('student.db')

	with con:
		cur = con.cursor()
		cursor = cur.execute("SELECT * FROM student")
		rows = []
		#columns = []

		for row in cursor:
			rows.append(row)
		#for col in cursor:
		#	column.append(col)

		return render_template('view.html',title='Display',rows=rows)	
