from skimage.measure import compare_ssim
from scipy.misc import imread
import numpy as np

img1 = imread('decode_image_100.png')
img2 = imread('raw_image_100.png')

img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))

print(img2.shape)
print(img1.shape)
ssim = compare_ssim(img1, img2, multichannel=True)

print(ssim)