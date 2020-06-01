import sys
import re
from FileReader import FileReader
from KnowledgeBase import KnowledgeBase
from Sentence import Sentence
from TruthTable import TruthTable

if __name__ == "__main__":
    """
    print('Number of arguments: ' + str(len(sys.argv)) + ' arguments.', end=' ')
    print('Argument List:' + str(sys.argv))
    """
    tell, ask = FileReader.read("test2.txt")
    
    if len(tell) == 0:
        print("No tell found.")
        sys.exit(0)
    if not ask:
        print("No ask found.")
        sys.exit(0)

    kb = KnowledgeBase(tell)

    tt = TruthTable(kb)

    print(tt.solve(ask))

    #sentence = Sentence("a&b&c=>d")

    #print(sentence.symbols)
    #print(sentence.parent)
    #print(sentence.child)

    #test_bool = sentence.solve({'a': False, 'b': True,'c': True,'d': False})
    #print(test_bool)

    #test = ['a', '&', 'b', '&', 'c', '=>', 'd']


    #print(tell)
    #print(ask)



