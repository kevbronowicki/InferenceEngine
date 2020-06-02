from Sentence import Sentence
from HornForm import HornForm


class KnowledgeBase:
    def __init__(self, sentences, type):
        self.sentences = []
        self.symbols = []
        self.type = type
        for sentence in sentences:
            self.tell(sentence)

    def tell(self, sentence):
        if self.type is 'HF':
            new = HornForm(sentence)
        else:
            new = Sentence(sentence)
        self.sentences.append(new)
        for symbol in new.symbols:
            if symbol not in self.symbols:
                self.symbols.append(symbol)

    def ask(self):
        pass
