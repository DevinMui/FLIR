from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
from skimage.io import imread
image = imread('flir.jpg')
image_gray = rgb2gray(image)

blobs_doh = blob_doh(image_gray, min_sigma=20, max_sigma=35, threshold=.01)

blobs_list = [blobs_doh]
print blobs_list
colors = ['lime']
titles = ['Determinant of Hessian']
sequence = zip(blobs_list, colors, titles)

fig,axes = plt.subplots(1, 3, sharex=True, sharey=True, subplot_kw={'adjustable':'box-forced'})
axes = axes.ravel()
for blobs, color, title in sequence:
    ax = axes[0]
    axes = axes[1:]
    ax.set_title(title)
    ax.imshow(image, interpolation='nearest')
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color=color, linewidth=2, fill=False)
        ax.add_patch(c)

plt.show()