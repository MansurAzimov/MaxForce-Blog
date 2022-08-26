from datetime import datetime
import email

from flask import render_template, request

from core import app

@app.route('/')
def base():
    return render_template('/base.html') 

@app.route('/index.html')
def index():
    return render_template('/index.html') 
    
@app.route ('/forum.html', methods = ['POST', 'GET'] )
def forum():
    return render_template ('forum.html')

@app.route('/video.html')
def video():
    return render_template('video.html')    

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/posts.html')
def posts():
    return render_template('posts.html')   

@app.route('/single-standard.html')
def singlestandard():
    return render_template('single-standard.html')   


@app.route ('/signup.html',methods = ['POST', 'GET'])
def signup():
    if request.method == 'POST':
        name = request.form.get ('name')
        email = request.form.get ('email')
        password = request.form.get ('password')
        email = request.form.get ('name')
        confirm_password = request.form.get ('confirm_password')
        if confirm_password == password:
            with open ('usert.txt', 'a', encoding='utf-8') as f:
                 f.write (str({'name':name, 'email':email, 'password':password}))
        else:
            return f'{confirm_password} != {password}'
    return render_template('signup.html')   

@app.route('/login.html')
def login():
    return render_template('login.html')  