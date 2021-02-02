import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from flask import Flask, request
from utils.create_hash import create_int_to_word
import pickle
import numpy
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow import keras

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
model = keras.models.load_model('xd_loss0.4299/xd_loss0.4299')
word_to_int_loaded = pickle.load(open("xd_loss0.4299/xd_loss0.4299/word2int.p", "rb"))
int_to_word_loaded = create_int_to_word(word_to_int_loaded)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
  data = request.json
  embedded = embed([data["string"]])
  outputboi = model.predict(embedded.numpy()) # 1 * 6000
  outputboi = tf.math.argmax(outputboi, axis=1)
  result = int_to_word_loaded[int(outputboi.numpy()[0])]
  return { "word": result }

if __name__ == '__main__':
  app.run(host="127.0.0.1", port=5000)