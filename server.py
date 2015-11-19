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
from flask_qiniustorage import Qiniu

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
QINIU_ACCESS_KEY = '-9GvtvlzlYsJThtrNMVocrhcsh3lmOTAuY6aXEBT'
QINIU_SECRET_KEY = 'l7fqBwgd-3M5ApcquLCFb-KKmLmNcIrlpQGJbBem'
QINIU_BUCKET_NAME = 'jpg2ascii'
QINIU_BUCKET_DOMAIN = '7xogjf.com1.z0.glb.clouddn.com'
app = Flask(__name__)
app.config.from_object(__name__)

qiniu_store = Qiniu(app)

if 'heroku' in os.environ.get("_", 'None'):
    jp2a = "/app/bin/jp2a"
else:
    jp2a = "source /etc/profile ; jp2a"


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

        jpg_name = uuid.uuid1().hex + '-' + jpg.filename
        jpg_path = 'http://%s/%s' % (app.config['QINIU_BUCKET_DOMAIN'], jpg_name)
        ret, info = qiniu_store.save(jpg, jpg_name)

        background = "dark" if request.form.get("is_dark", None) else "light"
        status, out = commands.getstatusoutput("%s %s --background=%s --width=68"\
                % (jp2a, jpg_path, background ))

        if status == 0:
            return render_template('index.html',
                output=out,
                status=True)
        else:
            return render_template('index.html', 
                    error_message=out, 
                    status=False)
    if request.method == "GET":
        return render_template('index.html', 
                status=u"尽量选择颜色比较单一的JPG")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


