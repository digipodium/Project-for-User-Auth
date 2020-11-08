from flask.globals import request
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from project_orm import User
from utils import *

from flask import Flask,session,flash,redirect,render_template,url_for

app = Flask(__name__)
app.secret_key = "the basics of life with python"
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
sess = Session()



@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html',title='login')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')
        if name and len(name) >= 3:
            if email and validate_email(email):
                if password and len(password)>=6:
                    if cpassword and cpassword == password:
                        try:
                            newuser = User(name=name,email=email,password=password)
                            sess.add(newuser)
                            sess.commit()
                            flash('registration successful','success')
                            return redirect('/')
                        except:
                            flash('email account already exists','danger')
                    else:
                        flash('confirm password does not match','danger')
                else:
                    flash('password must be of 6 or more characters','danger')
            else:
                flash('invalid email','danger')
        else:
            flash('invalid name, must be 3 or more characters','danger')
    return render_template('signup.html',title='register')

@app.route('/forgot',methods=['GET','POST'])
def forgot():
    return render_template('forgot.html',title='forgot password')

@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html',title='Home')

@app.route('/about')
def about():
    return render_template('about.html',title='About Us')

@app.route('/logout')
def logout():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


