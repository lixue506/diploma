#-*- coding:utf-8 -*-

from flask import Flask, render_template,request,flash,redirect,session
# from flask_login import login_required,LoginManager,login_user
# from function_tool import check_login
from query import *
import base64
import random
import datetime
import os
from flask import jsonify
import importlib,sys
importlib.reload(sys)

# request 获得form：一般post参数， values：get，post参数， args:get参数

app = Flask(__name__)
app.secret_key = b'#$ds2FG<3d3G6[F#&T_5#y2L"F4Q8z\n\xec]/'
# 首页
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
# 查询
@app.route('/Query', methods=['POST','GET'])
def Query():
    kind = request.values['kind']
    q = request.values['query']
    result = Query(kind, q)
    return jsonify(result)
# 证书显示
# @app.route('/Show/license/<userid>')
# def show_image(userid):
#     img_stream = return_img_stream(img_path)
#     return render_template('index.html',
#                            img_stream=img_stream)
# 证书下载
@app.route('/download/license/<string:filename>', methods=['GET'])
def download(filename):
    if request.method == "GET":
        if os.path.isfile(os.path.join('upload', filename)):
            return send_from_directory('upload', filename, as_attachment=True)
        pass
@app.route('/Login', methods=['POST','GET'])
def Login():
    if request.method == 'GET':
        name = request.values['name']
        pwd = request.values['pwd']
        result = Operator_mysql.Login_Judge(name, pwd)
        return jsonify({"status":str(result)})
    return render_template('Admin/Login.html')
@app.route('/Admin/index', methods=['GET', 'POST'])
def Admin_index():
    return render_template("admin/index.html")
@app.route('/Admin/edit', methods=['GET', 'POST'])
def Edit_manager():
    if request.method == 'GET':
        name = request.values['name']
        pwd = request.values['pwd']
        result = Operator_mysql.Register(name, pwd)
        return jsonify({"status":str(result)})
@app.route("/admin/lodout")
def logout():
    pass
# 证书上传
@app.route('/admin/upload',methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        basepath = os.path.dirname(__file__)
        son_path = "static\\{}\\".format(datetime.date.today())
        upload_path = os.path.join(basepath, son_path)
        if not os.path.exists(upload_path):
            os.mkdir(upload_path)
        # 图片上传
        f = request.files['images_file']
        f.save(os.path.join(upload_path, f.filename))

        #名单上传
        f = request.files['excel_file']
        f.save(os.path.join(upload_path, f.filename))

        return jsonify({"status":str(1)})

# 证书生成



if __name__ == '__main__':
    app.run(port=8000)





