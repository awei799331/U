import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from flask import Flask, request
from flask_cors import CORS, cross_origin
from utils.create_hash import create_int_to_word
import pickle
import numpy
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow import keras

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
model = keras.models.load_model('xd_2-9gramslowest/xd_2-9gramslowest')
word_to_int_loaded = pickle.load(open("word2int.p", "rb"))
int_to_word_loaded = create_int_to_word(word_to_int_loaded)

app = Flask(__name__)
CORS(app, support_credentials=True)
@cross_origin(supports_credentials=True)

@app.route("/predict", methods=["POST"])
def predict():
  try:
    data = request.json
    embedded = embed([data["string"]])
    outputboi = model.predict(embedded.numpy()) # 1 * 6000
    outputboi = tf.math.argmax(outputboi, axis=1)
    result = int_to_word_loaded[int(outputboi.numpy()[0])]
    return { "word": result }
  except:
    return 'error', 500

if __name__ == '__main__':
  app.run(host="127.0.0.1", port=5000)
