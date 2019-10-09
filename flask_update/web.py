#-*- coding:utf-8 -*-

from flask import Flask, render_template,request,flash,redirect,session
# from .function_tool import query
from flask import jsonify
import importlib,sys
importlib.reload(sys)

# request 获得form：一般post参数， values：get，post参数， args:get参数

app = Flask(__name__)
app.secret_key = 'NavigateyourcodewitheaseInselectpublicrepositoriesyoucannowclickonfunctionandmethodcalls'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/Query', methods=['POST','GET'])
def Query():
    kind = request.values['kind']
    q = request.values['query']
    return jsonify({1:{'id':"17121202036", 'times':"20190823", 'name':"张三", 'score':"58", 'click':"点击查看"}})

@app.route('/Login', methods=['POST'])
def Login():
    pass


if __name__ == '__main__':
    app.run(port=8000)





