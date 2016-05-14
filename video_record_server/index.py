from flask import Flask
import picamera
app = Flask(__name__)

camera = picamera.PiCamera()

@app.route("/")
def hello():
	camera.start_recording('video.h264')
	return "Hello World!"

@app.route("/")
def hello():
	camera.stop_recording
	return "Hello World!"

if __name__ == "__main__":
	app.run()