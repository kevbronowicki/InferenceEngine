from KnowledgeBase import KnowledgeBase
from Sentence import Sentence

class BackwardChaining:
    """description of class"""
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.count = 0

    def __proove(self, kb, removed, subgoals, q):
        print('query: ', q)
        print('subgoals: ', subgoals)
        print('removed: ', removed)
        for sentence in kb.sentences:
            if len(sentence.left) == 0 and q == sentence.right:
                return True
        removed.append(q)
        if q in subgoals:
            subgoals.remove(q)
        for sentence in kb.sentences:
            if q == sentence.right:
                # check if all conjuncts of goal to proove is not already in subgoals
                test = all(conjunct not in (removed or subgoals) for conjunct in sentence.left)
                if test:
                    for conjunct in sentence.left:
                        subgoals.append(conjunct)
                    if all(self.__proove(kb, removed, subgoals, conjunct) for conjunct in sentence.left):
                        return True

        return False

    def __bc_entails(self, kb, q):
        for sentence in kb.sentences:
            if len(sentence.left) == 0 and q == sentence.right:
                return True, [q]

        premises = []
        established = []
        subgoals = []
        removed = []
        chain = []

        return self.__proove(kb, subgoals, removed, q), []

        #for sentence in kb.sentences:
            #if q == sentence.right:
                #for conjunct in sentence.left:
                    #if conjunct not in subgoals:
                        #subgoals.append(conjunct)

        #while len(subgoals) != 0:
            #p = subgoals.pop(0)
            #chain.append(p)
        
        

    def solve(self, q):
        solution_found, chain = self.__bc_entails(self.knowledge_base, q)
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