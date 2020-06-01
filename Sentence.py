import re #for regular expressions

class Sentence:
    def __init__(self, sentence):
        ## fields ##
        self.symbols = []   # symbols within the sentence
        self.root = []      # root atomic sentence which child atomic sentences branch from
        self.atomic = {}    # dictionary of atomic sentences within sentence

        # separate connectives and symbols
        original = re.split("(=>|&|\(|\)|~)",sentence)
        # remove empty string
        while("" in original) : 
            original.remove("") 

        #extract symbols from sentence
        symbols = re.findall("[^(=>|&|\(|\)|~)]", sentence)
        self.symbols = list(set(symbols))  # remove duplicate symbols
        print("print symbols test: ", self.symbols)

        # extract child & sentences
        self.root = self._parse(original)
        print('root: ', self.root)
        print('atom: ', self.atomic)

    def _parse(self, sentence):
        # parse atomic sentences in brackets first
        while '(' in sentence:
            #index of left bracket in sentence
            left_index = sentence.index('(')
            # used for counting number of left and right brackets
            left_count = 1
            right_count = 0
           
            #search sentence for index of matching right bracket
            right_index = 0
            for i in range(left_index+1, len(sentence)):
                if sentence[i] is '(':
                    left_count+=1
                elif sentence[i] is ')':
                    right_count+=1
                # when counts match, the matching right bracket is found
                if left_count == right_count:
                    right_index = i
                    break
            if (right_index == 0):
                raise Exception("Incorrect braces format in sentence: ", sentence)
            # get section of sentence contained inside brackets
            section = sentence[left_index+1:right_index]
            # recursively call _parse till no brackets left
            section = self._parse(section)
            # replace section of sentence with name of atomic sentence
            if len(section) == 1:
                sentence[left_index] = section[0]
                del sentence[left_index+1:right_index+1]
            else:
                raise Exception("Incorrect senction format: ", section)

        ## create atomic sentences in order of precedence ##
        # negation
        while '~' in sentence:
            index = sentence.index('~')
            self._add_atom(index, sentence, '~')
        # conjunction and disjunction
        while ('&' or '||') in sentence:
            if '&' in sentence:
                index = sentence.index('&')
            if '||' in sentence:
                if sentence.index('||') < index:
                    index = sentence.index('||')
            self._add_atom(index, sentence, '&||')
        # implication
        while ('=>') in sentence:
            index = sentence.index('=>')
            self._add_atom(index, sentence, '=>')
        # biconditional
        while ('<=>') in sentence:
            index = sentence.index('<=>')
            self._add_atom(index, sentence, '<=>')

        return sentence

    # adds atomic sentence to atomic dictionary where the
    # key is of the format atom[n]
    # e.g. 'atom1' : ['a', '&', 'b']
    def _add_atom(self, index, sentence, connective):
        # negation is different as only has 2 elements
        if connective == '~':
            atom = [sentence[index],
                    sentence[index+1]]
            # create key from atomic sentence
            atom_key = "atom"+str(len(self.atomic)+1)
            # add atomic sentence to dictionary
            self.atomic.update({atom_key:atom})
            # add reference to atomic sentence in main sentence
            # and delete remaining symbols
            sentence[index] = atom_key
            del sentence[index+1]
        else:
            atom = [sentence[index-1],
                    sentence[index],
                    sentence[index+1]]
            atom_key = "atom"+str(len(self.atomic)+1)
            self.atomic.update({atom_key:atom})
            sentence[index-1] = atom_key
            del sentence[index:index+2]

    # solve sentence using the passed in model
    def solve(self, model):
        bool_pairs = {}
        # check if model has bool value for all symbols
        if all(symbol in model for symbol in self.symbols):
            # add symbol and its boolean value to dictionary: bool_pairs
            for symbol in self.symbols:
                bool_pairs.update({symbol:model[symbol]})
        else:
            raise Exception("No boolean for all symbols.")
        # perhaps label children with operation eg and1, or2
        # solve children and update bool pairs
        for key in self.atomic:
            # solve negation
            if len(self.atomic[key]) == 2:
                right =bool_pairs[self.atomic[key][1]]
                bool_pairs.update({key: not right})
            elif len(self.atomic[key]) == 3:
                left = bool_pairs[self.atomic[key][0]]
                right = bool_pairs[self.atomic[key][2]]
                # solve conjunction
                if self.atomic[key][1] == '&':
                    bool_pairs.update({key: left and right })
                # solve disjunction
                elif self.atomic[key][1] == '||':
                    bool_pairs.update({key: left or right })
                # solve implication
                elif self.atomic[key][1] == '=>':
                    bool_pairs.update({key: not left or right})
                # solve biconditional
                elif self.atomic[key][1] == '<=>':
                    bool_pairs.update({key: left == right})
            else:
                raise Exception("Atomic sentence in incorrect format: ", self.atomic[key])
        
        # return root atomic sentence which contains solution
        return bool_pairs[self.root[0]]