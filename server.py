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

@app.route('/upload', methods=('POST',))
def upload():
    """上传文件并转化为ASCII接口"""
    image = request.files.get("image")
    dark = request.form.get("dark")
    bucket = 'http://' + app.config['QINIU_BUCKET_DOMAIN']

    name = uuid.uuid1().hex + '.jpg'
    path = '%s/%s' % (bucket, name)
    qiniu_store.save(image, name)

    background = "dark" if dark=='true' else "light"
    status, output = commands.getstatusoutput(
            "%s %s"
            " --background=%s"
            " --width=68"
            % (jp2a, path, background)
            )
    return output


@app.route('/', methods=('GET', ))
def home():
    """JPG2ASCII首页"""
    return render_template('index.html', 
        status=u"尽量选择颜色比较单一的JPG")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


