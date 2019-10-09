#-*- coding:utf-8 -*-

from flask import Flask, render_template
# request 获得form：一般post参数， values：get，post参数， args:get参数

app = Flask(__name__)
app.secret_key = 'NavigateyourcodewitheaseInselectpublicrepositoriesyoucannowclickonfunctionandmethodcalls'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8000)





