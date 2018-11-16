#coding: utf8
import os
import base64
from flask import Flask
from flask import Response, jsonify, request, render_template
from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()

dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, static_url_path=dir_path)

@app.route('/')
def index():
    print 'get index'
    f = open('/Users/yangyou/Downloads/zkb-2.jpg')
    content = f.read()
    base64_content = base64.b64encode(content)
    imgdata = 'data:image/jpeg;base64,' + base64_content
    return render_template('index.html', pic_number=3, imgdata = imgdata)


# /photo?cam=3
@app.route("/photo")
def photo():
    result = {}
    camid = request.args.get('cam', default = 1, type = int)
    result['code'] = 10000
    result['cam'] = camid
    return jsonify(result)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8088)
    
    port = 8088
    http_server = WSGIServer(('', port), app)
    print 'listening on: %d'%(port)
    http_server.serve_forever()
