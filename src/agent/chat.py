import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import random
import pickle

class Chat:
    def __init__(self, dataset, chat_model_path, tokenizer_path, label_encoder_path):
        self.dataset = dataset
        self.chat_model_path = chat_model_path
        self.tokenizer_path = tokenizer_path
        self.label_encoder_path = label_encoder_path

        with open(dataset) as file:
            self.data = json.load(file)

    def chat(self, txt):
        # load trained model
        model = keras.models.load_model(self.chat_model_path)

        # load tokenizer object
        with open(self.tokenizer_path, 'rb') as handle:
            tokenizer = pickle.load(handle)

        # load label encoder object
        with open(self.label_encoder_path, 'rb') as enc:
            lbl_encoder: LabelEncoder = pickle.load(enc)

        # parameters
        max_len = 20

        result: np.array = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([txt]),
                                                truncating='post', maxlen=max_len))
        intent_key = lbl_encoder.inverse_transform([np.argmax(result)])[0]

        # Check if phrase is not highly recognizable (similar to default)
        label_index = lbl_encoder.transform(np.array(["default"]))
        default_weight = result[0][label_index]
        if(default_weight > 0.001):
            intent_key = "default"

        #print(sorted((r,i) for (_,i), r in np.ndenumerate(result)))

        return random.choice(self.data[intent_key]["responses"])