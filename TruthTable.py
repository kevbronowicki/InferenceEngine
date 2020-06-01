from KnowledgeBase import KnowledgeBase
class TruthTable:
    """description of class"""
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def solve(self, ask):
        #model_size = len((self.knowledge_base.symbols))
        models = {}
        solutions_found = 0
        solution_found = False
        for symbol in self.knowledge_base.symbols:
            models.update({symbol:False})
        
        for i in range(2 ** len(models)):
            for index, key in enumerate(models):
                models.update({key:i >> index & 1})
            #print(i)
            #print(models)
            all_true = True
            for sentence in self.knowledge_base.sentences:
                if not sentence.solve(models):
                    all_true = False
             
            if all_true & models[ask]:
                solutions_found+=1
                solution_found = True

            found = "YES" if solution_found else "NO"

        return found + ": " + str(solutions_found)

