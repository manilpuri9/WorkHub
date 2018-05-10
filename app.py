from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from data import Articles
from flask_mysqldb import MySQL
from wtforms.widgets import TextArea
from wtforms import Form, StringField,IntegerField, TextAreaField, PasswordField, validators, RadioField
from passlib.hash import sha256_crypt
from functools import wraps


app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'manil'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

# Index
@app.route('/')
def index():
    return render_template('home.html')


# #About
# @app.route('/add_worker_details')
# def add_worker_details():
#     return render_template('add_worker_details.html')

# About
@app.route('/about')
def about():
    return render_template('about.html')

# How it works

@app.route('/how_it_works')
def works():
    return render_template('how_it_works.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap


# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
    register_as = RadioField('Register as: ', choices = [('1','User'), ('2','Worker')])

# worker info class
class WorkerInfoForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=50),validators.DataRequired()])
    name = StringField('Name', [validators.Length(min=1, max=50),validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    category = StringField('Category', [validators.Length(min=4, max=25),validators.DataRequired()])
    jobtitle = StringField('Jobtitle', [validators.Length(min=4, max=25),validators.DataRequired()])
    experiance = IntegerField('Experiance', [validators.NumberRange(min=0, max=50)])
    phone = IntegerField('Telephone',)
    address = StringField('Address')
    availability = StringField('Availability')
    description = StringField('Description',)
#######################################################
#######################################################
class CommentForm(Form):
        email = StringField('Email')


# WorkersDetails
@app.route('/workerDetails/<string:username>/', methods=['GET', 'POST'])
def workerDetails(username):
    form = CommentForm(request.form)
    if request.method == 'POST' and form.validate():
         c = mysql.connection.cursor()


        
     # Create cursor
    cur = mysql.connection.cursor()
    cur1 = mysql.connection.cursor()
    # Get articles
    cur.execute("SELECT * FROM workerD WHERE username = %s",[username])
    workers = cur.fetchall()
    cur1.execute("SELECT * FROM workerR WHERE username = %s",[username])
    comments = cur1.fetchall()
    
    return render_template('workerDetails.html',workers=workers,comments=comments)
    cur1.close()
    cur.close()


# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        registerdata = form.register_as.data
        print(registerdata)
        if registerdata =='1':
            # Create cursor
            cur = mysql.connection.cursor()

            # Execute query
        
            cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

            # Commit to DB
            mysql.connection.commit()

            # Close connection
            cur.close()

            flash('You are now registered user and can log in', 'success')
            return redirect(url_for('login_users'))

        else:
            # Create cursor
            cur = mysql.connection.cursor()

            # Execute query
        
            cur.execute("INSERT INTO workers(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
            cur.execute("INSERT INTO workerD(username, name, email, address, category, jobtitle, experiance, description, likes,dislikes, availability, phone) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )",(username, name, email, 'Enter Address', 'Enter Category', 'Enter Job Title', '0', 'Add your descriptions here...', '0', '0', '0', '0'))

            # Commit to DB
            mysql.connection.commit()

            # Close connection
            cur.close()

            flash('You are now registered worker and can log in', 'success')

            return redirect(url_for('login_workers'))
    return render_template('register.html', form=form)

# Edit Worker details
@app.route('/add_worker_details/<string:username>/', methods=['GET', 'POST'])
@is_logged_in
def add_worker_details(username):
    
    form = WorkerInfoForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        category = form.category.data
        jobtitle = form.jobtitle.data
        experiance = form.experiance.data
        phone = int(form.phone.data)
        address = form.address.data
        availability = int(form.availability.data)
        description = form.description.data
        likes = int(12345)
        dislikes =int(12)
        print(phone, availability,likes,dislikes)
        cur1 = mysql.connection.cursor()
        result = cur1.execute("SELECT* FROM workerD WHERE username = %s",[username])
        cur1.close()
        if result > 0:
            #Create cursor
            cur = mysql.connection.cursor()
            # Execute query
            cur.execute("UPDATE workerD SET name =%s, email=%s, address=%s, category=%s, jobtitle =%s, experiance=%s, description =%s, likes=%s, dislikes = %s, availability =%s, phone=%s WHERE username = %s", (name,      email,   address,     category,    jobtitle,     experiance,       description, likes,    dislikes,         availability, phone,           username))
            # Commit to DB
            mysql.connection.commit()
            # Close connection
            cur.close()
        
        else:
            #Create cursor
            cur = mysql.connection.cursor()
            # Execute query                                                                                                                                           %s, %s, %s, %s, %s, %s, %s, %s, %d, %d, %d, %d                                        
            cur.execute("INSERT INTO workerD(username, name, email, address, category, jobtitle, experiance, description, likes,dislikes, availability, phone) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )",(username, name, email, address, category, jobtitle, experiance, description, likes, dislikes, availability, phone))
            # Commit to DB
            mysql.connection.commit()
            # Close connection
            cur.close()
        flash('Great, we have your details now.', 'success')
        return redirect(url_for('dashboard_workers'))

    cur1 = mysql.connection.cursor()
    cur1.execute("SELECT * FROM workerD WHERE username= %s",[username])
    workers = cur1.fetchall()
    if(workers >0 ):
        return render_template('add_worker_details.html', form=form, workers=workers)
    else:
        cur1.execute("SELECT * FROM workerD WHERE username= %s",'0')
        workers = cur1.fetchall()
    
    cur1.close()

# User login
@app.route('/login_users', methods=['GET', 'POST'])
def login_users():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username
                session['register_as'] = '1'


                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard_users'))
                #return redirect(url_for('testUserDashboard'))
            else:
                error = 'Invalid login'
                return render_template('login_users.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login_users.html', error=error)

    return render_template('login_users.html')


# User login
@app.route('/login_workers', methods=['GET', 'POST'])
def login_workers():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM workers WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username
                session['register_as'] = '2'

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard_workers'))
            else:
                error = 'Invalid login'
                return render_template('login_workers.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login_workers.html', error=error)

    return render_template('login_workers.html')



# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return render_template('home.html')

# Users Dashboard
@app.route('/dashboard_users')
@is_logged_in
def dashboard_users():

    #Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    result = cur.execute("SELECT * FROM workerD" )

    workersfound = cur.fetchall()

    if result > 0:
        return render_template('testUserDashboard.html', workersfound=workersfound)
    else:
        msg = 'No Workers Found'
        return render_template('testUserDashboard.html', msg=msg)
    # Close connection
    cur.close()

# Workers Dashboard
@app.route('/dashboard_workers/')
@is_logged_in
def dashboard_workers():
        return render_template('dashboard_workers.html')


if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
    
