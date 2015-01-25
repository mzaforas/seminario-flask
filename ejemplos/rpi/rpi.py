import picamera
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flash')
def flash():
    camera = picamera.PiCamera()
    camera.capture('static/photo.jpg')
    camera.close()
    return render_template('photo.html')

app.run(debug=True, host='0.0.0.0', port=5000)
