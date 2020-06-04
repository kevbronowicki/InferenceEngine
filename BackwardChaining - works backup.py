from KnowledgeBase import KnowledgeBase
from Sentence import Sentence

class BackwardChaining:
    """description of class"""
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.count = 0

    def __proove(self, kb, subgoals, removed, established, q):
        print('query: ', q)
        
        print('removed: ', removed)
        print('established: ', established)

        for sentence in kb.sentences:
            if len(sentence.left) == 0 and q == sentence.right:
                established.append(q)
                subgoals.remove(q)
                print('established: ', established)
                print('exited true1: ', q)
                return True, established
        removed.append(q)
        if q in subgoals:
            subgoals.remove(q)

        for sentence in kb.sentences:
            if q == sentence.right:
                all_true = True
                print('conjuncts: ', sentence.left)
                for conjunct in sentence.left:
                    print('subgoal:', subgoals)
                    print('removed: ', removed)
                    print('conjunct: ', conjunct)
                    if conjunct in established:
                        print(conjunct, ' is established!')
                        continue
                    if conjunct in removed:
                        all_true = False
                        print(conjunct, ' is removed!')
                        break
                    if conjunct in subgoals:
                        all_true = False
                        print(conjunct, ' is subgoal!')
                        break
                    subgoals.append(conjunct)
                    print('subgoals: ', subgoals)
                    isEstablished, established = self.__proove(kb, subgoals, removed, established, conjunct)
                    if not isEstablished:
                        all_true = False
                if all_true:
                    established.append(q)
                    print('established: ', established)
                    print('exited true2: ', q)
                    return True, established

        print('exited false: ', q)
        return False, established

    def __bc_entails(self, kb, q):
        for sentence in kb.sentences:
            if len(sentence.left) == 0 and q == sentence.right:
                return True, [q]

        premises = []
        established = []
        subgoals = []
        removed = []

        subgoals.append(q)

        return self.__proove(kb, subgoals, removed, established, q)

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