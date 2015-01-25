import os
import picamera
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flash')
def flash():
    PHOTO_PATH = 'static/photo.jpg'

    try:
        os.remove(PHOTO_PATH)
    except OSError:
        pass

    camera = picamera.PiCamera()
    camera.capture(PHOTO_PATH)
    camera.close()

    return render_template('photo.html')

app.run(debug=True, host='0.0.0.0', port=5000)
