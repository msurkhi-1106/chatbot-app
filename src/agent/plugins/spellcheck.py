from plugins.agent_plugin import AgentPlugin
import nltk
import re

class SpellCheck(AgentPlugin):
    def parse(self, query):
        dictionary = nltk.corpus.words.words()
        wordList = re.findall(r'\w+', query)
        
        correct_query = ""
        
        for word in wordList:
            word = nltk.stem.porter.PorterStemmer().stem(word)
            temp = [(nltk.edit_distance(word, w),w) for w in dictionary if w[0]==word[0]]
            correct_query += sorted(temp, key = lambda val:val[0])[0][1] + " "
        
        print(correct_query)
        
        return correct_query