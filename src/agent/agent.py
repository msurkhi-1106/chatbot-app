import nltk
nltk.download('popular')

class Agent:
    def query(self, query) -> str:

        #TODO: Spelling Check, call a function within agent to fix the query to realistic words --GABE or whoever gets to it

        #TODO Part of speach tagging --Nathan
        query = self.pos_tag(query)
        
        #TODO: Named Entity Recognition: Recognize names given and append 
        #saying "hello" or "tell jessica to" or something to the front --GABE
        entitySet = self.entity_recognition(query)

        #TODO: COReference: Figure out if the query is about the user or their patient is talking about --Jordan C


        ##TODO??? Other things to cover our bases if it's easy

        ####TODODODO: Add all of the sections, and return Dr phils smart answer to the query all 3

        return str(entitySet)
    
    def pos_tag(self, query):
        token = nltk.word_tokenize(query)
        tagged = nltk.pos_tag(token)
        
        return tagged

        
    def entity_recognition(self, query) -> str:
        named_ent = nltk.ne_chunk(query, binary=True)
        
        ne_set = []

        for i in namedEnt:
            if type(i) == nltk.tree.Tree:
                neSet.append(i)
            
        print(ne_set)
        return ne_set
