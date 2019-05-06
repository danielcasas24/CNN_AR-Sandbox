# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 17:15:32 2019

@author: Andres
"""

import numpy as np
import cv2
import  imutils
contador = 0
#folder = ['a','e','i','o', 'u','c']
#identificador = ['','','','','','']
folder = ['tr','cu']
identificador = ['','']
cropB = True

def colorspace(image,cropBool):
    # Rotate
    rotated = imutils.rotate(image,180)
    # End Rotate

    # Saturation
    bgr = [47, 122, 16]
    thresh = 40
    minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
    maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])
    maskBGR = cv2.inRange(image,minBGR,maxBGR)
    resultBGR = cv2.bitwise_and(image, image, mask = maskBGR)
    # End Saturation

    # Crop
    height = np.size(resultBGR, 0)
    width = np.size(resultBGR, 1)
    new_width_remaining = width - height
    crop_img = resultBGR[0:height, (new_width_remaining//2):width-(new_width_remaining//2)]
    # End Crop
    return crop_img
