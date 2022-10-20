import numpy as np
import cv2
import matplotlib.pyplot as plt
#import webcolors
import matplotlib.colors as mc
import time
from PIL import Image, ImageOps
#from keras.models import load_model
import pyzbar.pyzbar as pyzbar
# import tensorflow.python
from os import listdir
from os.path import isfile, join
from os.path import exists
import os
import sys
import argparse
import pytesseract
from djitellopy import Tello
from DetectShapes.detect_shapes_OpenCV import DetectUtils
from DetectShapes.detect_shapes_OpenCV import DetectScreenInFrame
import logging
import threading
from Main_Tello_Simon import TelloControl


timing_img = 10
dirpath = r"C:\Users\davidra\Desktop\NINJA_RAFAEL\Ninja_Symon2\first_try20"
filename = "frame_1_Screen detected, screen mode is 2" + ".jpg"
full_path = os.path.join(dirpath, filename)
img = cv2.imread(full_path)
cv2.imshow("photo", img)  # optional display photo
cv2.waitKey(0)
debugTello = TelloControl(dirpath=dirpath, debug=True)
debugTello.ImageProcessing.original_image = img
# PlotCv2ImageWithPlt(self.ImageProcessing.screen, 'screen to analyze')
debugTello.ImageProcessing.DetectScreen(True)
flag, value = debugTello.AnalyzePicture()
print(flag)

