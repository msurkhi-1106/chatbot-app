from ast import parse
from collections import deque
from functools import reduce
import nltk
import re
from chat import chat

from plugins.agent_plugin import AgentPlugin
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Agent:
    def __init__(self, plugins, nltk_dependencies):
        print("Downloading nltk dependencies")
        for dependency in nltk_dependencies:
            nltk.download(dependency)

        self.plugins = list(map(lambda x: x(), plugins))

    def query(self, query) -> str:
        print(set(self.synonyms("ball", "n")))
        return chat(query)

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
   
    
    ## self.synonyms(word, pos_tag) returns list of synonyms for inputted word with the pos_tag
    ## has error catching now
    def synonyms(self, word, pos_tag):
        word = word.lower()
        try:
            synonyms = set()
            synonyms.add(word)
            valid_sets = [s for s in wordnet.synsets(word, pos = pos_tag) if s.name().startswith(word)]
            while len(synonyms) < 3 and valid_sets:
                syn_set = valid_sets.pop(0)
                print(syn_set)
                if syn_set.name().startswith(word):
                    for l in syn_set.lemmas():
                        name = l.name().replace("_", " ")
                        synonyms.add(name.lower())
            
            print(synonyms)

            return synonyms
        except:
            print("Encountered an error; make sure you inputted a valid word to get synonyms.")
            return word