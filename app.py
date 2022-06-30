from flask import Flask, render_template, Response, request
import pandas as pd
from flask_cors import CORS
import pickle
from camera import VideoCamera

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/monmaps')
def monmap():
    return render_template('monmap.html')


@app.route('/aiobj')
def aiobj():
    return render_template('aiobj.html')


@app.route('/setsen')
def setsen():
    return render_template('setsensor.html')


@app.route('/managepage')
def manpage():
    return render_template('adminpage.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
