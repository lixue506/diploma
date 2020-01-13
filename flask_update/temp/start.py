from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, "static\\images\\")
        f.save(os.path.join(upload_path,f.filename))
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(port=5000)