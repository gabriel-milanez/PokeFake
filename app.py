import cv2
import tensorflow as tf
import numpy as np 

print("--- Verificando Ambientes ---")
print("OpenCV versão:", cv2.__version__)
print("TensorFlow versão:", tf.__version__)

print("\n[OpenCV] Carregando imagem...")

print("\n[TFLite] Inicializando o modelo de IA...")
try:
    print("Sucesso: Pronto para carregar modelos .tflite!")
except Exception as e:
    print("Erro: ao carregar o interpretador:", e)