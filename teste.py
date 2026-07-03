import cv2
print ("OpenCV instalado com sucesso! Versão:", cv2.__version__)

import tensorflow as tf
interpreter = tf.lite.interpreter(model_path="seu_modelo.tflite")
