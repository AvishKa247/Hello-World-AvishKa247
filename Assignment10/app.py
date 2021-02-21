import mysql
import mysql.connector
from flask import Flask, render_template, blueprints, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/')
def home():
    return redirect('/assignment10')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost', user='root', password='root', database='webproject')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    if query_type == 'commit':
        connection.commit()
        return_value = True
    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result
    connection.close()
    cursor.close()
    return return_value


@app.route('/assignment10')
def assignment10():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    print(query_result)
    return render_template('Assignment10.html', users=query_result)


@app.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        query = "INSERT into users (fullname, email) VALUES ('%s', '%s')" % (fullname, email)
        interact_db(query, query_type='commit')
        return redirect('/assignment10')
    if request.method == 'GET':
        email = request.args['email']
        fullname = request.args['fullname']
        query = "UPDATE users SET fullname = '%s' where email='%s';" % (fullname, email)
        interact_db(query, 'commit')
        return redirect('/assignment10')
    return render_template('Assignment10.html', req_method=request.method)


@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        email = request.args['email']
        query = "DELETE FROM users where email='%s';" % email
        interact_db(query, 'commit')
        return redirect('/assignment10')
    return 'User was Deleted'


if __name__ == '__main__':
    app.run()
