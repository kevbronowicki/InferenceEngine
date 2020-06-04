from KnowledgeBase import KnowledgeBase
from Sentence import Sentence

class BackwardChaining:
    """description of class"""
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.count = 0

    def __prove(self, kb, removed, chain, goal):
        print('query: ', goal)
        print('removed: ', removed)
        print('chain: ', chain)

        for sentence in kb.sentences:
            if len(sentence.conjuncts) == 0 and goal == sentence.head:
                chain.append(goal)
                print('chain: ', chain)
                print('exited true1: ', goal)
                return True, chain
        
        removed.append(goal)

        for sentence in kb.sentences:
            if goal == sentence.head:
                all_true = True     # check for if all subgoals are proven
                print('conjuncts: ', sentence.conjuncts)
                for subgoal in sentence.conjuncts:
                    print('removed: ', removed)
                    print('conjunct: ', subgoal)
                    # check if subgoal has already been proven true
                    if subgoal in chain:
                        print(subgoal, ' is chain!')
                        continue
                    # check if subgoal has already failed
                    if subgoal in removed:
                        all_true = False
                        print(subgoal, ' is removed!')
                        break
                    established, chain = self.__prove(kb, removed, chain, subgoal)
                    if not established:
                        all_true = False
                # goal is proven true if subgoals
                if all_true:
                    chain.append(goal)
                    print('chain: ', chain)
                    print('exited true2: ', goal)
                    return True, chain

        print('exited false: ', goal)
        return False, chain

    def __bc_entails(self, kb, goal):
        for sentence in kb.sentences:
            if len(sentence.conjuncts) == 0 and goal == sentence.head:
                return True, [goal]
        chain = []
        removed = []
        return self.__prove(kb, removed, chain, goal)


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