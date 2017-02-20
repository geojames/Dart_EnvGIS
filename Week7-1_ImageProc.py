#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
__author__ = 'James T. Dietrich'
__contact__ = 'james.t.dietrich@dartmouth.edu'
__copyright__ = '(c) James Dietrich 2016'
__license__ = 'MIT'
__date__ = 'Wed Nov 16 11:33:39 2016'
__version__ = '1.0'
__status__ = "initial release"
__url__ = "https://github.com/geojames/..."

"""
Name:           Week8-1_ImageProc.py
Compatibility:  Python 3.5
Description:    This program does stuff

URL:            https://github.com/geojames/...

Requires:       libraries

Dev ToDo:

AUTHOR:         James T. Dietrich
ORGANIZATION:   Dartmouth College
Contact:        james.t.dietrich@dartmouth.edu
Copyright:      (c) James Dietrich 2016

"""
#------------------------------------------------------------------------------

from __future__ import absolute_import
import os
from scipy import ndimage as ndi
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt

os.chdir('c:/Users/James/Dropbox/Teaching/2015/Code/')

#%% Multi-dimensional image processing (scipy.ndimage)

# sample images

ascent = misc.ascent()
lena = misc.lena()
face = misc.face()

plt.subplot(1,2,1)
plt.imshow(face)
plt.subplot(1,2,2)
plt.imshow(ascent, cmap='gray')

# READING IMAGES
#   flatten option reduces to 1-band gray scale image
flor_rgb = ndi.imread('images/florence2.jpg')
flor_gray = ndi.imread('images/florence2.jpg', flatten=True)

plt.figure()
plt.subplot(1,2,1)
plt.imshow(flor_rgb)
plt.subplot(1,2,2)
plt.imshow(flor_gray,cmap='gray')

# Basic Image properties

flor_rgb.shape  # image shape Y,X,bands
flor_rgb.ndim   # number of dimentions (bands)
flor_rgb.dtype  # data type (8-bit for most jpegs (0-255))
flor_rgb.min()  # Min and Max values
flor_rgb.max()

# Individual Bands
# 3-dim array indexing: image[:,:,band_num]

fig = plt.figure()
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.imshow(flor_rgb[:,:,0],cmap='gray')
ax1.set_title('RED')
ax2.imshow(flor_rgb[:,:,1],cmap='gray')
ax2.set_title('GREEN')
ax3.imshow(flor_rgb[:,:,2],cmap='gray')
ax3.set_title('BLUE')
ax4.imshow(flor_rgb)
ax4.set_title('RGB')

# Image manipulation

# cropping (using indexing)
#   same basic syntax as numpy array indexing, but...
#       the the dimensions ar [Y,X]
crop_flor = flor_rgb[180:370,315:440]
plt.imshow(crop_flor)

# Other array-like manipulations
# flipping - left/right and up/down
plt.figure()
plt.subplot(1,2,1)
plt.imshow(np.fliplr(flor_rgb))
plt.subplot(1,2,2)
plt.imshow(np.flipud(flor_rgb))

# Rotation
#   reshapes the image to keep the whole thing
flor_rotate = ndi.rotate(flor_rgb, 45)

#   keeps the original image dimensions
flor_rotate_shape = ndi.rotate(flor_rgb, 60, reshape = False)

plt.figure()
plt.subplot(1,2,1)
plt.imshow(flor_rotate)
plt.subplot(1,2,2)
plt.imshow(flor_rotate_shape)

#%% Filtering Filtering

# min/max/median filters

flor_min = ndi.minimum_filter(flor_gray,size=(3,3))
flor_max = ndi.maximum_filter(flor_gray,size=(3,3))
flor_med = ndi.median_filter(flor_gray,size=(3,3))

flor_max_rgb = ndi.maximum_filter(flor_rgb,size=(3,3,3))

# Gaussian blurring

flor_gauss = ndi.gaussian_filter(flor_gray,sigma = 3)

# Convolution Filtering
#   Using a custom kernel to manipulate an image and enhance or blur an image

k = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])    # 3x3 sharpening
flor_sharp = ndi.convolve(flor_gray,k)

k = np.array([[-1,0,1], [-1,0,1], [-1,0,1]])    # 3x3 vertical edges
flor_vert = ndi.convolve(flor_gray,k)
plt.imshow(flor_vert, cmap ='seismic')

k = np.array([[-1,-1,-1], [0,0,0], [1,1,1]])    # 3x3 horz edges
flor_horz = ndi.convolve(flor_gray,k)
plt.imshow(flor_horz, cmap ='PuOr')

k = np.array([[-2,-1,-1], [-1,1,1], [0,1,2]])    # 3x3 emboss
flor_emboss = ndi.convolve(flor_gray,k)
plt.imshow(flor_emboss, cmap='gray')

k = np.array([[-2,-1,0,1,2], [-2,-1,0,1,2], [-2,-1,0,1,2]])    # 5x5 vertical edges
flor_vert_big = ndi.convolve(flor_gray,k)
plt.imshow(flor_vert_big, cmap ='seismic')

# feature extraction
# laplacian edge detection
flor_laplace = ndi.laplace(flor_gray)

# Sobel Edge detection
flor_sobel = ndi.sobel(flor_gray,mode='constant')

sx = ndi.sobel(flor_gray, axis=0, mode='constant')
sy = ndi.sobel(flor_gray, axis=1, mode='constant')
sob = np.hypot(sx, sy)

#%%

# OTHER IMAGE PROCESSING LIBRARIES

# Scikit Image (preinstalled with Anaconda)
#   http://scikit-image.org/
import skimage

# Python Image Library (PIL or Pillow) - (preinstalled with Anaconda)
#   http://pillow.readthedocs.io/en/4.0.x/index.html
import PIL

# Open Computer Vision (OpenCV) - requires install
#   http://opencv.org/
#   http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html


