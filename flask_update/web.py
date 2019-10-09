#-*- coding:utf-8 -*-

from flask import Flask, render_template,request,flash,redirect,session
from flask_login import login_required
# from .function_tool import query
from flask import jsonify
import importlib,sys
importlib.reload(sys)

# request 获得form：一般post参数， values：get，post参数， args:get参数

app = Flask(__name__)
app.secret_key = 'NavigateyourcodewitheaseInselectpublicrepositoriesyoucannowclickonfunctionandmethodcalls'

@app.before_request
def before_request():
    pass

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/Query', methods=['POST','GET'])
def Query():
    kind = request.values['kind']
    q = request.values['query']
    return jsonify({1:{'id':"17121202036", 'times':"20190823", 'name':"张三", 'score':"58",'rank':"5", 'click':"点击查看"}})

@app.route('/Login', methods=['POST','GET'])
def Login():
    return render_template('admin/Login.html')

@app.route('/Login/Judge', methods=['GET','POST'])
def Login_Judge():
    name = request.values['name']
    pwd = request.values['pwd']
    if pwd == '123':
        return jsonify({"status":"1"})
    else:
        return jsonify({"status":"0"})

@login_required
@app.route('/Admin/index', methods=['GET', 'POST'])
def Admin_index():
    return render_template("admin/index.html")


if __name__ == '__main__':
    app.run(port=8000)





