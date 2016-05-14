from matplotlib import pyplot as plt
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
from skimage.io import imread
import requests

url = "http://52.90.77.195"
# get video from flir or infinite loop
image = imread('flir.jpg') # gonna be frame
image_gray = rgb2gray(image) # convert frame

blobs_doh = blob_doh(image_gray, min_sigma=20, max_sigma=35, threshold=.01) # detect frame

if len(blobs_doh):
	print "request to server here to drone"
	r = requests.get(url + "/intrude")
	# potentially move to blob
	y = blobs_doh[0][0]
	x = blobs_doh[0][1]
	# also start recording video

else:
	r = requests.get(url + "/no_intrude")
	# set drone to standalone mode/passive tracking