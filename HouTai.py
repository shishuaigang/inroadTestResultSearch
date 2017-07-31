# coding=utf-8
import pymssql
from flask import Flask, Response, render_template, request, redirect, jsonify

from Prepare import Prepare

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/detail', methods=["POST", "get"])
def detail():
    data = Prepare("1", "1", "1").detail()
    return jsonify(data)


@app.route('/search', methods=["POST"])
def search():
    bt = request.form.get('begintime')
    et = request.form.get('endtime')
    name = request.form.get('apiname')
    p = Prepare(bt, et, name)
    p.sql_sentence()
    p.create_qushitu()
    with open('qushi.png', 'rb') as f:
        return Response(f.read(), mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
