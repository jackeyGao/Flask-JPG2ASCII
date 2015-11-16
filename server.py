# -*- coding: utf-8 -*-
'''
File Name: web.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: 五 11/13 16:11:23 2015
'''
import os
import commands
import uuid
from flask import Flask
from flask import make_response
from flask import abort, redirect, url_for
from flask import request
from flask import render_template
from werkzeug import secure_filename


UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__),'uploads')
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == "POST":
        jpg = request.files.get("jpg", None)
        if not jpg:
            return render_template('index.html', 
                    error_message=u"没有指定文件",
                    status=False)
        if not allowed_file(jpg.filename):
            return render_template('index.html', 
                    error_message=u"仅支持jpeg,jpg",
                    status=False)

        jpg_name = uuid.uuid1().hex + '.' + jpg.filename.rsplit('.', 1)[1]
        jpg_path = os.path.join(app.config['UPLOAD_FOLDER'], jpg_name)
        jpg.save(jpg_path)

        background = "dark" if request.form.get("is_dark", None) else "light"
        status, out = commands.getstatusoutput("source /etc/profile; jp2a %s \
                --background=%s --width=68" % (jpg_path, background ))

        if status == 0:
            return render_template('index.html',
                output=out,
                status=True)
        else:
            return render_template('index.html', 
                    error_message=out, 
                    status=False)
    else:
        return render_template('index.html', 
                status=u"尽量选择颜色比较单一的JPG")

if __name__ == '__main__':
    app.run(debug=True)

