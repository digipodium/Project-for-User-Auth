import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from project_orm import User

from flask import Flask,session,flash,redirect,render_template,url_for

app = Flask(__name__)
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
sess = Session()

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html',title='login')

@app.route('/signup',methods=['GET','POST'])
def signup():
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


