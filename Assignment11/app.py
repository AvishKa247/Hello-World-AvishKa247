import mysql
import mysql.connector
from flask import Flask, render_template, blueprints, request, redirect, url_for, flash, jsonify

Assignment11 = blueprints('Assignment11', __name__)


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


@Assignment11.route('/Assignment11/users', methods=['GET', 'POST'])
def num11():
    if request.method == 'GET':
        query = "select * from users"
        query_result = interact_db(query=query, query_type='fetch')
        if len(query_result) == 0:
            return jsonify({
                'success': 'false', "data": []
            })
        else:
            return jsonify({
                'success': 'true', "data": query_result
            })
    return 'Opps That went wrong'


@Assignment11.route('/Assignment11/users/selected', defaults={'SOME_USER_ID': 8})
@Assignment11.route('/Assignment11/users/selected/<int:SOME_USER_ID>', methods=['GET', 'POST'])
def selected(SOME_USER_ID):
    if request.method == 'GET':
        query = "select * from users where id = '%s';" %SOME_USER_ID
        query_result = interact_db(query=query, query_type='fetch')
        if len(query_result) == 0:
            return jsonify({
                'success': 'false', "data": []
            })
        else:
            return jsonify({
                'success': 'true', "data": query_result
            })
    return 'Opps That went wrong'
