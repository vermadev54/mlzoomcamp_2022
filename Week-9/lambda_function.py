#!/usr/bin/env python
# coding: utf-8

from io import BytesIO
from urllib import request
from PIL import Image
import tflite_runtime.interpreter as tflite
import numpy as np

interpreter = tflite.Interpreter(model_path='dino-vs-dragon-v2.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img



def prepare_input(x):
    return x / 255.0


def lambda_handler(event,context):
    

    url = event.get('url')
    img = download_image(url)
    img = prepare_image(img, target_size=(150, 150))
    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = prepare_input(X)
    
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    predict = preds[0].tolist()
    print(event)
    return {'prediction':predict}