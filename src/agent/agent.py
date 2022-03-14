import nltk
class Agent:
    def query(self, query) -> str:

        #TODO: Spelling Check, call a function within agent to fix the query to realistic words --GABE or whoever gets to it

        #TODO Part of speach tagging --Nathan
        
        query = nltk.word_tokenize(query)
        query = nltk.pos_tag(query)
        
        #TODO: Named Entity Recognition: Recognize names given and append 
        #saying "hello" or "tell jessica to" or something to the front --GABE
        
        #TODO: COReference: Figure out if the query is about the user or their patient is talking about --Jordan C


        ##TODO??? Other things to cover our bases if it's easy

        ####TODODODO: Add all of the sections, and return Dr phils smart answer to the query all 3

        return query