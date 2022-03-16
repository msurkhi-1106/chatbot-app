from ast import parse
from collections import deque
from functools import reduce
import nltk
import re

from plugins.agent_plugin import AgentPlugin
nltk.download('popular')
nltk.download('vader_lexicon')
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Agent:
    def __init__(self, plugins):
        self.plugins = list(map(lambda x: x(), plugins))

    def query(self, query) -> str:
        print(self.plugins)
        #TODO: Spelling Check, call a function within agent to fix the query to realistic words --GABE or whoever gets to it
        check = self.plugins[0].parse(query)
        #TODO Part of speach tagging --Nathan
        pos_tag = self.plugins[1].parse(query)
        #TODO: Named Entity Recognition: Recognize names given and append
        ne_rec = self.plugins[2].parse(pos_tag) 
        #sentiment analysis
        sentiment = self.plugins[3].parse(query)

        ##TODO Sentiment for easy interchangeable sentences

        ####TODODODO: Add all of the sections, and return Dr phils smart answer to the query all 3

        #seethe and cope

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