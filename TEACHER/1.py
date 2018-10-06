from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charts.html')
def charts():
    return render_template('charts.html')

@app.route('/elements.html')
def elements():
    return render_template('elements.html')

@app.route('/icons.html')
def icons():
    return render_template('icons.html')

@app.route('/notifications.html')
def notifications():
    return render_template('notifications.html')

@app.route('/page-lockscreen.html')
def page_lockscreen():
    return render_template('page-lockscreen.html')

@app.route('/page-login.html')
def page_login():
    return render_template('page-login.html')


@app.route('/page-profile.html')
def page_profile():
    return render_template('page-profile.html')

@app.route('/panels.html')
def panels():
    return render_template('panels.html')

@app.route('/tables.html')
def tables():
    return render_template('tables.html')

@app.route('/typography.html')
def typography():
    return render_template('typography.html')

@app.route('/index.html')
def index1():
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)