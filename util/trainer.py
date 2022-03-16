import json 
import numpy as np 
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Embedding, GlobalAveragePooling1D, LSTM, Dropout
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import pickle

class Trainer:
    def __init__(self, input_file):
        self.input_file = input_file
    
    def train(self):
        with open(self.input_file) as file:
            data = json.load(file)
        
        training_sentences = []
        training_labels = []
        labels = []
        responses = []


        for i, intent in enumerate(data):
            for pattern in intent['patterns']:
                training_sentences.append(pattern)
                training_labels.append(i)
            responses.append(intent['responses'])
            
            labels.append(i)
                
        num_classes = len(labels)

        lbl_encoder = LabelEncoder()
        lbl_encoder.fit(training_labels)
        training_labels = lbl_encoder.transform(training_labels)

        vocab_size = 50000
        embedding_dim = 16
        max_len = 20
        oov_token = "<OOV>"

        tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token) # adding out of vocabulary token
        tokenizer.fit_on_texts(training_sentences)
        word_index = tokenizer.word_index
        sequences = tokenizer.texts_to_sequences(training_sentences)
        padded_sequences = pad_sequences(sequences, truncating='post', maxlen=max_len)

        embedding_vector_features=45

        model=Sequential()

        model.add(Embedding(vocab_size,embedding_vector_features,input_length=max_len))

        model.add(LSTM(128,activation='relu',return_sequences=True))

        model.add(Dropout(0.2))

        model.add(LSTM(128,activation='relu'))

        model.add(Dropout(0.2))

        model.add(Dense(32,activation='relu'))

        model.add(Dropout(0.2))

        model.add(Dense(num_classes,activation='softmax'))

        model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])


        epochs = 550
        history = model.fit(padded_sequences, np.array(training_labels), epochs=epochs)

        # saving model
        model.save("chat_model")

        # saving tokenizer
        with open('tokenizer.pickle', 'wb') as handle:
            pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
            

        # saving label encoder
        with open('label_encoder.pickle', 'wb') as ecn_file:
            pickle.dump(lbl_encoder, ecn_file, protocol=pickle.HIGHEST_PROTOCOL)