from KnowledgeBase import KnowledgeBase
from Sentence import Sentence

class TruthTable:
    """description of class"""
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.count = 0

    def __tt_entails(self, kb, alpha):
        #print('kb symbols: ', kb.symbols)
        #print('alpha symbols: ', alpha.symbols)
        symbols = kb.symbols
        for symbol in alpha.symbols:
            if symbol not in symbols:
                symbols.append(symbol)
        #print('all symbols: ', symbols)
        return self.__tt_check_all(kb, alpha, symbols, {})


    def __tt_check_all(self, kb, alpha, symbols, model):
        #print('model: ', model)
        if len(symbols) == 0:
            all_true = True
            for sentence in kb.sentences:
                #print('kb sentence: ', sentence.original)
                #print(model)
                if not sentence.solve(model):
                    all_true = False
            if all_true:
                alpha_solution = alpha.solve(model)
                if alpha_solution:
                    self.count+=1
                return alpha_solution
            else:
                return True
        else:
            p = symbols[0]
            rest = symbols[1:]
            model1 = model.copy()
            model1.update({p:True})
            model2 = model.copy()
            model2.update({p:False})
  
            #print('model1: ', model1)
            #print('model2: ', model2)
            return (self.__tt_check_all(kb, alpha, rest, model1) and 
                    self.__tt_check_all(kb, alpha, rest, model2))


    def solve(self, ask):
        #model_size = len((self.knowledge_base.symbols))
        alpha = Sentence(ask)
        solution_found = self.__tt_entails(self.knowledge_base, alpha)
       
        solutions_found = self.count

        found = "YES" if solution_found else "NO"

        return found + ": " + str(solutions_found)

    def oldsolve(self, ask):
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