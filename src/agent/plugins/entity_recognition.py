from plugins.agent_plugin import AgentPlugin
import nltk

class EntityRecognition(AgentPlugin):
    def parse(self, query):
            named_ent = nltk.ne_chunk(query, binary=True)
        
            ne_set = []
            for i in named_ent:
                if type(i) == nltk.tree.Tree:
                    st = ""
                    for j in range (len(i)):
                        st = st + " " + i[j][0]
                    ne_set.append(st.strip())
            return ne_set