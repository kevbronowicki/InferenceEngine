# Horn-form sentence class
import re #for regular expressions

class HornForm:
    def __init__(self, sentence):
        ## fields ##
        self.clause = []
        self.symbols = []
        self.right = ""
        self.left = []

        # separate connectives and symbols
        self.clause = re.split("(=>|&|\(|\)|~|\|\||<=>)",sentence)
        # remove empty string
        while("" in self.clause) : 
            self.clause.remove("") 
        # remove brackets
        while("(" in self.clause) : 
            self.clause.remove("(") 
        while(")" in self.clause) : 
            self.clause.remove(")") 
        # check horn form connectives
        if ('~' or '||' or '<=>') in self.clause:
            raise Exception("Sentence is not in horn form ", self.clause)
        
        # get right symbol
        #print('clause: ', self.clause)
        if len(self.clause) == 1:
            self.right = self.clause[0]
        else:
            index = self.clause.index('=>')
            temp = self.clause[index+1:]
            if (len(temp) > 1):
                raise Exception("Error horn form format", self.clause)
            self.right = temp[0]
            del temp
            # get left
            temp = self.clause[:index]
            if (temp[0] or temp[-1]) is '&':
                raise Exception("Error horn form format", self.clause)
            for i in range(len(temp)-1):
                if temp[i] == temp[i+1]:
                    raise Exception("Error horn form format", self.clause)
            for ele in temp:
                if ele is not '&':
                    self.left.append(ele)
            self.symbols = self.left.copy()
        if self.right not in self.symbols:
            self.symbols.append(self.right)
        #print('left: ', self.left)
        #print('right: ', self.right)
