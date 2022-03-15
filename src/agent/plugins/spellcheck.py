from plugins.agent_plugin import AgentPlugin
import nltk
import re
import spellchecker

class SpellCheck(AgentPlugin):
    def parse(self, query):
        spell = spellchecker.SpellChecker(distance = 4)
        wordList = re.findall(r'\w+', query)
        
        correct_query = ""
        
        for word in wordList:
            correct_query += spell.correction(word) + " "
        
        print(correct_query)
        
        return correct_query