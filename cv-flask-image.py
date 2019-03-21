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

photoFolder = os.path.dirname(os.path.realpath(__file__))


@app.route("/test")
def test():
    print('get test')
    time.sleep(0.1)
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

def photo_n():
    result = {'res': 'failed'}
    try:
        camid = request.args.get('cam', default = 0, type = int)
        print 'camid: ' + str(camid)
        cap = capMap[camid]
        for i in range(5):
            ret, frame = cap.read()
        if ret:    
            nowYearMonthDay = time.strftime("%Y%m%d")
            parentPath = os.path.join(photoFolder, nowYearMonthDay)
            print('parentpath: ', parentPath)
            if not os.path.exists(parentPath):
                os.mkdir(parentPath)
            nowtimestampString = time.strftime("%Y%m%d%H%M%S")
            filename = nowtimestampString + '_{camid}.jpg'.format(camid=camid)
            fullpath = os.path.join(parentPath, filename)
            cv2.imwrite(fullpath, frame)
            ret, jpgcontent = cv2.imencode('.jpg', frame)
            if ret:
                command = 'ls {parentPath}/*_{camid}.jpg | wc -l'.format(parentPath=parentPath, camid=camid)
                pic_number = os.popen(command).read()
                pic_number = pic_number.strip()

                base64_content = base64.b64encode(jpgcontent)
                imgdata = 'data:image/jpeg;base64,' + base64_content

                return render_template('index.html', pic_number=pic_number, imgdata = imgdata)       
            return jsonify(result)
    except Exception as e:
        print e
        return jsonify(result)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8088)
    http_server = WSGIServer(('', 8088), app)
    http_server.serve_forever()
