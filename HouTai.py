# coding=utf-8
from flask import Flask, Response, render_template

import readDATA

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<apiname>/')
def result(apiname):
    fullurl = readDATA.readDATA("Inroad_Test_Result", "192.168.31.99\\sql2012", "sgshi", "ssg12345!", "").split_url()
    spliturl = []
    for i in range(len(fullurl)):
        temp = fullurl[i].split('/')
        spliturl.append(temp[2])
    zidian = dict(zip(spliturl, fullurl))

    readDATA.readDATA("Inroad_Test_Result", "192.168.31.99\\sql2012", "sgshi", "ssg12345!",
                      zidian[apiname]).create_qushitu()
    with open('qushi.png', 'rb') as f:
        return Response(f.read(), mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
