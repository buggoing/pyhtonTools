import os
import time
import cv2
from flask import Flask
from flask import Response, jsonify
from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()
app = Flask(__name__)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


@app.route("/test")
def test():
    print('get test')
    return "Hello World! from gbot pic server"

@app.route("/filephoto")
def filephoto():
    with open('photo.jpg') as f:
        content = f.read()
        resp = Response(content)
        resp.headers['Content-Type'] = 'image/jpeg'
        return resp
        
@app.route("/photo")
def photo():
        result = {}
        for i in range(2):
            ret, frame = cap.read()
        if ret:
            ret, jpgcontent = cv2.imencode('.jpeg', frame)
            if ret:
                resp = Response(jpgcontent.tostring(), content_type="image/jpeg")
                return resp
            result = {'res': 'failed'}

        return jsonify(result)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8088)
    http_server = WSGIServer(('', 8088), app)
    http_server.serve_forever()
