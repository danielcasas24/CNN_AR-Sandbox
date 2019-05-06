# -*- coding: utf-8 -*-
import numpy as np
import cv2
import glob
from keras.utils import to_categorical

def cargar_datos(URLbase, lista_carpetas):
    temp_datos = []
    numero_elementos=len(glob.glob(URLbase+'/'+lista_carpetas[0]))
    for i in range(len(carpeta)):
        for j in range(1,(numero_elementos+1))
            image = cv2.imread(URLbase+'/'+folder[i]+'/'+str(j)+'.png')
            image = cv2.resize(image, dsize=(128,128),interpolation=cv2.INTER_NEAREST)
            temp_datos.append(image)
    datos = np.array(temp_datos)
    return datos

def generar_target(lista_carpetas, datos):
    temp_target = []
    numero_elementos=len(glob.glob(URLbase+'/'+lista_carpetas[0]))
    clases = np.arange(len(lista_carpetas))
    for i in range(len(lista_carpetas)):
        for j in range(numero_elementos):
            temp_target.append(clases[i])
    target = np.array(temp_target)
    return target

def procesar_datos(datos_entrenamiento, target_entrenamiento, datos_prueba, target_prueba):
    clases = np.unique(datos)
    numero_clases = len(clases)
    nRows,nCols,nDims = datos_entrenamiento.shape[1:]
    datos_entrenamiento = datos_entrenamiento.reshape(datos_entrenamiento.shape[0], nRows, nCols, nDims)
    datos_prueba = datos_prueba.reshape(datos_prueba.shape[0], nRows, nCols, nDims)
    datos_entrenamiento = datos_entrenamiento.astype('float32')
    datos_prueba = datos_prueba.astype('float32')
    datos_entrenamiento  /= 255
    datos_prueba /= 255
    target_entrenamiento = keras.utils.to_categorical(target_entrenamiento, num_classes)
    target_prueba = keras.utils.to_categorical(target_prueba, num_classes)
    return datos_entrenamiento, target_entrenamiento, datos_prueba, target_prueba
