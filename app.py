from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'kjcse'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

#Articles = Articles()

# Index
@app.route('/')
def index():
    return render_template('home.html')

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

@app.route('/student')
@is_logged_in
def student_data():#navbar student ka hoga in card layout
    return render_template('student.html')

@app.route('/student_track')
@is_logged_in
def student_track():
    cur = mysql.connection.cursor()
    data = {}
    # Get articles8
    #result = cur.execute("SELECT * FROM student")
    if(cur.execute("SELECT s1 from student where login = %s", session["username"])):
        data['s1'] = cur.execute("SELECT attendance, tot_att FROM s1 where student_id = %s", session["username"])
        data['s1'] = cur.fetchall()
        if data['s1'][0]/data['s1'][1] * 100 > 70:
            data['s1'] = str(70/100* data['s1'][1]/data['s1'][0])
        else:
            data['s1'] = "safe"
    if(cur.execute("SELECT s2 from student where login = %s", session["username"])):
        data['s2'] = cur.execute("SELECT attendance, tot_att FROM s2 where student_id = %s", session["username"])
        data['s2'] = cur.fetchall()
        if data['s2'][0]/data['s2'][1] * 100 > 70:
            data['s2'] = str(70/100* data['s2'][1]/data['s2'][0])
        else:
            data['s2'] = "safe"
    if(cur.execute("SELECT s3 from student where login = %s", session["username"])):
        data['s3'] = cur.execute("SELECT attendance, tot_att FROM s3 where login = %s", session["username"])
        data['s3'] = cur.fetchall()
        if data['s3'][0]/data['s3'][1] * 100 > 70:
            data['s3'] =str( 70/100* data['s3'][1]/data['s3'][0])
        else:
            data['s2'] = "safe"
    

    
    return render_template('student_track.html', data=data)
    # Close connection
    cur.close()


@app.route('/student_committee')
@is_logged_in
def student_committee():
    cur = mysql.connection.cursor()
    data = {}
    c1 = []
    # Get articles
    #result = cur.execute("SELECT * FROM student")
    if(cur.execute("SELECT c1 from student where login = %s", session["username"])):
        c1 = cur.execute("SELECT m1,m2 FROM c1 where c_id = 1 ")
        c1 = cur.fetchall()
        data['c1'] = c1
        print(data['c1'])
    if(cur.execute("SELECT c2 from student where login = %s", session["username"])):
        c2 = cur.execute("SELECT m1,m2 FROM c1 where c_id = 2")
        c2 = cur.fetchall()
        data['c2'] = c2
        print(data['c2'])
    """
    if(cur.execute("SELECT c2 from student where login = %s", session["username"])):
        data['c2'] = cur.execute("SELECT m1,m2 FROM c2")
        data['c2'] = cur.fetchall()
        if data['c2'] == "":
            del data['c2']
    
    """
    if len(data)!=0:
        return render_template('student_committee.html', data=data)
    else:
        msg = 'No Notes'
        return render_template('student_committee.html', msg=msg)
    # Close connection
    cur.close()

@app.route('/student_notes')
@is_logged_in
def student_notes():
    cur = mysql.connection.cursor()
    data = {}
    s1=[]
    s2=[]
    s3=[]
    # Get articles
    #result = cur.execute("SELECT * FROM student")
    if(cur.execute("SELECT notes from s1 where student_id = %s", session["username"])):
        s1 = cur.execute("SELECT notes FROM s1 ")
        s1= cur.fetchall()
        data['s1'] = s1
        print(data['s1'])
        #if data['s1'] == "":
        #   del data['s1']
    ##return render_template('student_notes.html',s1=s1)

    if(cur.execute("SELECT notes from s2 where student_id = %s",session["username"])):
        s2 = cur.execute("SELECT notes FROM s2 ")
        s2= cur.fetchall()
        data['s2'] = s1
        print(data['s2'])
        """
        data['s2'] = cur.execute("SELECT notes FROM s1 LIMIT 1")
        data['s2'] = cur.fetchall()
        if data['s1'] == "":
            del data['s1']
        """
    if(cur.execute("SELECT notes from s3 where student_id = %s", session["username"])):
        s3 = cur.execute("SELECT notes FROM s3 ")
        s3= cur.fetchall()
        data['s3'] = s1
        print(data['s3'])
    if len(data)!=0:
        return render_template('student_notes.html', data=data)
    else:
        msg = 'No Notes'
        return render_template('student_notes.html', msg=msg)
    # Close connection

    cur.close()

@app.route('/student_submissions')
@is_logged_in
def student_submissions():
    cur = mysql.connection.cursor()
    data = {}
    s1 = []
    s2 = []
    s3 = []
    # Get articles
    #result = cur.execute("SELECT * FROM student")
    if(cur.execute("SELECT submission from s1 where student_id = %s", session["username"])):
        s1= cur.execute("SELECT submission FROM s1")
        s1 = cur.fetchall()
        data['s1'] = s1
    if(cur.execute("SELECT submission from s2 where student_id = %s", session['username'])):
        s2 = cur.execute("SELECT submission FROM s1")
        s2 = cur.fetchall()
        data['s2'] = s2
    if(cur.execute("SELECT submission from s3 where student_id = %s", session['username'])):
        s3 = cur.execute("SELECT submission FROM s1")
        s3 = cur.fetchall()
        data['s3'] = s3

    print(data)
    if len(data)!=0:
        return render_template('student_submissions.html', data=data)
    else:
        msg = 'Hurray, no submissions!'
        return render_template('student_submissions.html', msg=msg)
    # Close connection
    cur.close()


# About
@app.route('/about')
def about():
    return render_template('about.html')


# Articles
@app.route('/articles')
def articles():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall()

    if result > 0:
        return render_template('articles.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('articles.html', msg=msg)
    # Close connection
    cur.close()


#Single Article
@app.route('/article/<string:id>/')
def article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

    article = cur.fetchone()

    return render_template('article.html', article=article)


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


# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM student WHERE login = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']
           # print(sha256_crypt.checksum)

           # print(password_candidate)
           # print(password)
            # Compare Passwords
            if password == password_candidate:
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')


# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    # Create cursor
    cur = mysql.connection.cursor()
    return redirect(url_for('dashboard'))
"""
    # Get articles
    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall()

    if result > 0:
        return render_template('das*hboard.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('dashboard.html', msg=msg)
    # Close connection
    cur.close()

# Article Form Class
class ArticleForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])

# Add Article
@app.route('/add_article', methods=['GET', 'POST'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)",(title, body, session['username']))

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Article Created', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_article.html', form=form)
"""


# Edit Article
@app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article by id
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

    article = cur.fetchone()
    cur.close()
    # Get form
    form = ArticleForm(request.form)

    # Populate article form fields
    form.title.data = article['title']
    form.body.data = article['body']

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']

        # Create Cursor
        cur = mysql.connection.cursor()
        app.logger.info(title)
        # Execute
        cur.execute ("UPDATE articles SET title=%s, body=%s WHERE id=%s",(title, body, id))
        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Article Updated', 'success')

        return redirect(url_for('dashboard'))

    return render_template('edit_article.html', form=form)

# Delete Article
@app.route('/delete_article/<string:id>', methods=['POST'])
@is_logged_in
def delete_article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Execute
    cur.execute("DELETE FROM articles WHERE id = %s", [id])

    # Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('Article Deleted', 'success')

    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
