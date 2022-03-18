from ast import parse
from collections import deque
from functools import reduce
import nltk
import re
from chat import Chat

from plugins.agent_plugin import AgentPlugin
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Agent:
    def __init__(self, plugins, nltk_dependencies, dataset = "config/dataset.json", chat_model_path = "chat_model", tokenizer_path = "tokenizer.pickle", label_encoder_path = "label_encoder.pickle"):
        print("Downloading nltk dependencies")
        for dependency in nltk_dependencies:
            nltk.download(dependency)

        self.plugins = list(map(lambda x: x(), plugins))
        self.dataset = dataset
        self.chat = Chat(dataset, chat_model_path, tokenizer_path, label_encoder_path)

    def query(self, query) -> str:
        return self.chat.chat(query)

        print(self.plugins)
        #TODO: Spelling Check, call a function within agent to fix the query to realistic words --GABE or whoever gets to it
        check = self.plugins[0].parse(query)
        #TODO Part of speach tagging --Nathan
        pos_tag = self.plugins[1].parse(query)
        #TODO: Named Entity Recognition: Recognize names given and append
        ne_rec = self.plugins[2].parse(pos_tag) 
        #saying "hello" or "tell jessica to" or something to the front --GABE
        #TODO: COReference: Figure out if the query is about the user or their patient is talking about --Jordan C
        sentiment = self.plugins[3].parse(query)

        ##TODO Sentiment for easy interchangeable sentences
       # sentiment = self.sentiment_analysis(query)

        ####TODODODO: Add all of the sections, and return Dr phils smart answer to the query all 3

        return pos_tag

    
    def pos_tag(self, query):
        token = nltk.word_tokenize(query)
        tagged = nltk.pos_tag(token)
        
        return tagged
   
    
    ## self.synonyms(word) returns list of synonyms for inputted word
    ## if word is more than one word, returns list of synonyms for first word only
    ## has error catching now
    def synonyms(self, word):
        try:
            tag = self.pos_tag(word)
            if " " in word:
                tag = self.pos_tag(word.split()[0])
            synonyms = []
            for syn_set in wordnet.synsets(word):
                for l in syn_set.lemmas():
                    name = l.name().replace("_", " ")
                    testTag = self.pos_tag(name)
                    if testTag[0][1] == tag[0][1]:
                        name = name.lower()
                        synonyms.append(name)
            
            print(set(synonyms))

            return synonyms
        except:
            print("Encountered an error; make sure you inputted a valid word to get synonyms.")
            return word