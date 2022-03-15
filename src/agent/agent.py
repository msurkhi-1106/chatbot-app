from ast import parse
from collections import deque
from functools import reduce
import nltk
import re

from plugins.agent_plugin import AgentPlugin

class Agent:
    def __init__(self, plugins):
        self.plugins = list(map(lambda x: x(), plugins))

    def query(self, query) -> str:

        #TODO: Spelling Check, call a function within agent to fix the query to realistic words --GABE or whoever gets to it
        #TODO Part of speach tagging --Nathan
        #TODO: Named Entity Recognition: Recognize names given and append
        
        #TODO: COReference: Figure out if the query is about the user or their patient is talking about --Jordan C


        ##TODO??? Other things to cover our bases if it's easy

        ####TODODODO: Add all of the sections, and return Dr phils smart answer to the query all 3

        return reduce(lambda q, p: p.parse(q), self.plugins, query)