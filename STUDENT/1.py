from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def indexs():
    return render_template('notificationss.html')

@app.route('/chartss.html')
def chartss():
    return render_template('chartss.html')

@app.route('/elementss.html')
def elementss():
    return render_template('elementss.html')

@app.route('/iconss.html')
def iconss():
    return render_template('iconss.html')

@app.route('/notificationss.html')
def notificationss():
    return render_template('notificationss.html')

@app.route('/page-lockscreens.html')
def page_lockscreens():
    return render_template('page-lockscreens.html')

@app.route('/page-logins.html')
def page_logins():
    return render_template('page-logins.html')


@app.route('/page-profiles.html')
def page_profiles():
    return render_template('page-profiles.html')

@app.route('/panelss.html')
def panelss():
    return render_template('panelss.html')

@app.route('/tabless.html')
def tabless():
    return render_template('tabless.html')

@app.route('/typographys.html')
def typographys():
    return render_template('typographys.html')

@app.route('/indexs.html')
def index1s():
    return render_template('indexs.html')


if __name__=="__main__":
    app.run(debug=True)