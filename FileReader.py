class FileReader:
    @staticmethod
    def read(filename):
        tell = []
        ask = ''
        temp = []
        ask_found = False
        with open(filename) as f:
            # read a line at a time
            for line in f:
                # remove newline and separate statements by ;
                temp = line.strip().split(";") 
                # add statements to Result if not blank
                for x in temp:
                    x = x.lower()
                    if x != "" and x != "tell" and x != "ask":
                        if ask_found:
                            ask = x
                        else:
                            tell.append(x.replace(" ", ""))
                    if x == "ask":
                        ask_found = True
        return tell, ask

