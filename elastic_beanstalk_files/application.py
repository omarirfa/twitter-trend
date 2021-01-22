#!/usr/bin/env python
# coding: utf-8



#from flask import Flask,request,jsonify
import re
from flask import Flask,jsonify,request
from flask import render_template
import ast
application = Flask(__name__,template_folder='templates')
notfound = 404
invalid = 403
ok = 200
labels = []
values = []
@application.route("/")
def get_chart_page():
    global labels,values
    labels = []
    values = []
    return render_template('chart.html', values=values, labels=labels)
@application.route('/refreshData')
def refresh_graph_data():
    global labels, values
    print("labels now: " + str(labels))
    print("data now: " + str(values))
    return jsonify(sLabel=labels, sData=values)
@application.route('/updateData', methods=['POST'])
def update_data():
    global labels, values, ok, notfound
    if not request.form or 'data' not in request.form:
        return notfound
    labels = ast.literal_eval(request.form['label'])
    values = ast.literal_eval(request.form['data'])
    print("labels received: " + str(labels))
    print("data received: " + str(values))
    return ok
if __name__ == "__main__":
	application.run(port=5000, debug=True)
    #app.run(host='localhost', port=5000)