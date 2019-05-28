from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Checkmate-master:Checkmate-master@localhost:8889/Checkmate-master'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(20))
    last = db.Column(db.String(20))
    
    def __init__(self, first, last):
        self.first = first
        self.last = last

class Username(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(120))


    def __init__(self, name): 
        self.name = name

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    length = db.Column(db.String(1000))

    def __init__(id, length):
        self.length = length

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    star = db.Column(db.Integer, primary_key=True)

    def __init__(id, star):
        self.star = star
        
@app.route('/home')
def homepage():
    return render_template("homepage.html")
    
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify-password']
        num_of_errors = 0

        if len(username) < 3 or len(username) > 20:
            num_of_errors += 1
            flash('Username not valid.', 'error')
        if len(password) < 3 or len(password) > 20:
            num_of_errors += 1
            flash('Password not valid.', 'error')
        if password != verify_password:
            num_of_errors += 1
            flash('Passwords do not match.', 'error')
        

        if num_of_errors > 0:
            return redirect('/signup')
        else:
            session['username'] = username
            user = User(username, password)
            db.session.add(user)
            db.session.commit()
            return "Sign-Up Successful"

    return render_template('index.html', title = 'Checkmatep')

  
@app.route('/login')    
def login():
    return render_template("login.html")

@app.route('/adduser')
def adduser():
    return render_template("adduser.html")

@app.route('/addrating')
def addrating():
    return render_template("addrating.html")

if __name__ == '__main__':
    app.run()