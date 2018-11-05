#coding: utf8
from flask import Flask
from flask import Response, jsonify
from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World! from gbot pic server"

@app.route("/photo")
def photo():
    result = {}
    result['code'] = 10000
    return jsonify(result)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8088)
    http_server = WSGIServer(('', 8088), app)
    http_server.serve_forever()
