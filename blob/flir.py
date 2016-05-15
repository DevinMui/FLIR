from matplotlib import pyplot as plt
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
from skimage.io import imread
import requests
from pylepton import Lepton
import numpy as np
import time
import cv2
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)

start = 5

def capture(flip_v = False, device = "/dev/spidev0.1"):
	with Lepton(device) as l:
		a,_ = l.capture()
	if flip_v:
		cv2.flip(a,0,a)
	cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)
	np.right_shift(a, 8, a)
	return np.uint8(a)

url = "http://52.90.77.195"
# get video from flir or infinite loop
while True:
	cv2.imwrite("wat.jpg", capture())
	image = imread("wat.jpg") # gonna be frame
	image_gray = rgb2gray(image) # convert frame

	blobs_doh = blob_doh(image_gray, min_sigma=20, max_sigma=35, threshold=.01) # detect frame

	if len(blobs_doh):
		print "request to server here to drone"
		r = requests.get(url + "/intrude")
		pwm.ChangeDutyCycle(start + 15)
		start = start + 15
		time.sleep(0.5)
		# potentially move to blob
		y = blobs_doh[0][0]
		x = blobs_doh[0][1]
		# also start recording video

	else:
		r = requests.get(url + "/no_intrude")
		pwm.ChangeDutyCycle(5)
		#time.sleep(0.5)
		# set drone to standalone mode/passive tracking
