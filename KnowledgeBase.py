from Sentence import Sentence
class KnowledgeBase:
    def __init__(self, sentences):
        self.sentences = []
        self.symbols = []
        for sentence in sentences:
            self.tell(sentence)

    def tell(self, sentence):
        new = Sentence(sentence)
        self.sentences.append(new)
        self.symbols.extend(new.symbols)

    def ask(self):
        pass
