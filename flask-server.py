# coding: utf8
import sys
import os
import base64
import time
import cv2
import json
from flask import Flask
from flask import Response, jsonify, request, render_template
from werkzeug.serving import WSGIRequestHandler

from usb_camera_client import CameraClient
# from gevent import monkey
# from gevent.pywsgi import WSGIServer

# 不打印一般日志
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
# monkey.patch_all()

camClient = CameraClient(0)
dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, static_url_path=dir_path)


@app.route('/')
def index():
    print('get index: ', time.time())
    f = open('./test.jpg')
    content = f.read()
    base64_content = base64.b64encode(content)
    imgdata = 'data:image/jpeg;base64,' + base64_content
    time.sleep(2)
    print('return: ', time.time())
    return jsonify({'code': 0})
    return render_template('index.html', pic_number=3, imgdata=imgdata)


# /photo?cam=3
@app.route("/photo")
def photo():
    result = {}
    camid = request.args.get('cam', default=1, type=int)
    result['code'] = 10000
    result['cam'] = camid
    time.sleep(2)
    return jsonify(result)


@app.route('/takephoto')
def takephoto():
    frame = camClient.getPhoto()
    ret, jpgcontent = cv2.imencode('.jpg', frame)
    if ret:
        base64_content = base64.b64encode(jpgcontent)
        imgdata = 'data:image/jpeg;base64,' + base64_content

        return render_template('index.html', imgdata = imgdata)

@app.route('/json')
def jsonTest():
    res = {'code': 0}
    resp = Response(json.dumps(res, ensure_ascii=False))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host='0.0.0.0', port=8088, threaded=True)
    # sys.exit()
    # port = 8088
    # http_server = WSGIServer(('', port), app)
    # print 'listening on: %d'%(port)
    # http_server.serve_forever()
