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
        #TODO: Spelling Check, call a function within agent to fix the query to realistic words --GABE or whoever gets to it
        taggedQuery = self.pos_tag(query)
        #TODO Part of speach tagging --Nathan
        #TODO: Named Entity Recognition: Recognize names given and append 
        #saying "hello" or "tell jessica to" or something to the front --GABE
        entitySet = self.entity_recognition(taggedQuery)
        #TODO: COReference: Figure out if the query is about the user or their patient is talking about --Jordan C


        ##TODO Sentiment for easy interchangeable sentences
        sentiment = self.sentiment_analysis(query)

        ####TODODODO: Add all of the sections, and return Dr phils smart answer to the query all 3

        return reduce(lambda q, p: p.parse(q), self.plugins, query)
    
    def pos_tag(self, query):
        token = nltk.word_tokenize(query)
        tagged = nltk.pos_tag(token)
        
        return tagged
      
    def entity_recognition(self, query):
        named_ent = nltk.ne_chunk(query, binary=True)
        
        ne_set = []
        for i in named_ent:
            if type(i) == nltk.tree.Tree:
                st = ""
                for j in range (len(i)):
                    st = st + " " + i[j][0]
                ne_set.append(st.strip())
        return ne_set
    
        
    def sentiment_analysis(self, query):
        sentiment = SentimentIntensityAnalyzer().polarity_scores(query)
        return sentiment['compound'] #return a value between -1 and 1 indicating negativity


        
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