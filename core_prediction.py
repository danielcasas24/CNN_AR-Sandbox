# -*- coding: utf-8 -*-
import cv2
import numpy as np
from keras.models import load_model
import wx
import pyttsx
import color_space as cs

engine = pyttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 110)
engine.setProperty('voice', 'spanish')
engine.setProperty('voice', voices[4].id)


clases = ['clase 1','clase 2', '...','Clase N']
clases = ['a','e','i','o','u']

model = load_model('modelo.h5')
model = load_model('modeloVocales.h5')


image = cv2.imread('screenshot.png')

image_processed = cs.colorspace(image)
image_resize = cv2.resize(image_processed, dsize=(128,128),
                            interpolation=cv2.INTER_NEAREST)
test_image = np.expand_dims(image_resize, axis = 0)


predictor = model.predict_classes(test_image)
prediction_class = predictor[0]
final_prediction = clases[prediction_class]

engine = pyttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 110)
engine.setProperty('voice', 'spanish')
engine.setProperty('voice', voices[4].id)


app = wx.App()
engine.say('Tu dibujo es '+str(clases[final_prediction]))
engine.runAndWait()
