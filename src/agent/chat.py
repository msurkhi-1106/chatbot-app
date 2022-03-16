import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import random
import pickle

with open("config/dataset.json") as file:
    data = json.load(file)


def chat(txt):
    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20

    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([txt]),
                                             truncating='post', maxlen=max_len))
    tag = int(lbl_encoder.inverse_transform([np.argmax(result)]))

    print(result)
    
    return random.choice(data[tag]["responses"])