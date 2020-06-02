from KnowledgeBase import KnowledgeBase
from Sentence import Sentence

class ForwardChaining:
    """description of class"""
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.count = 0

    def __fc_entails(self, kb, q):
        count = {}
        agenda = []
        chain = []
        for sentence in kb.sentences:
            if len(sentence.left) > 0:
                count.update({sentence:len(sentence.left)})
            else:
                agenda.append(sentence.right)
        inferred = {}
        for symbol in kb.symbols:
            inferred.update({symbol: False})

        while len(agenda) != 0:
            p = agenda.pop(0)
            chain.append(p)
            if not inferred[p]:
                inferred[p] = True
                for c in count:
                    if p in c.left:
                        count[c]-=1
                        if count[c] == 0:
                            if c.right == q:
                                chain.append(q)
                                return True, chain
                            agenda.append(c.right)
        return False, []


    def solve(self, q):
        solution_found, chain = self.__fc_entails(self.knowledge_base, q)
        solution = "YES" if solution_found else "NO"
        if solution_found:
            solution = "YES: "
            for ele in chain:
                if ele is chain[-1]:
                    solution += ele
                else:
                    solution += ele + ", "
        else:
            solution = "NO"
        return solution