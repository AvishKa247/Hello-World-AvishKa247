from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def home():
    return redirect(url_for('assignment9'))


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    search, username, = '', ''
    users = ({'fullname': "Dan Lewi", 'email': "DaniBoy@walla.co.il"},
             {'fullname': "Sarah Abrahahm", 'email': "Sarah12@Gmail.co.il"},
             {'fullname': "Ross Gellar", 'email': "FriendsLover@Gmail.co.il"},
             {'fullname': "Amit Tal", 'email': "Amit555@walla.co.il"})
    if request.method == 'POST':
        username = request.form['FullName']
        session['logged_in'] = True
        session['username'] = username
    if request.method == 'GET':
        if 'SearchField' in request.args:
            search = request.args['SearchField']
            return render_template('assignment9.html', search=search, users=users)
    return render_template('assignment9.html', request_method=request.method, username=username)


@app.route('/log_out')
def log_out():
    session['logged_in'] = False
    return redirect(url_for('assignment9'))


if __name__ == '__main__':
    app.run(debug=True)
