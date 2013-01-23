import re

class Obfuscator:
    input_str = ""
    words = []
    output_lines = []

    def __init__(self, s):
        self.input_str = s

    def add_terminal(self, m):
        print m.group(1)
        if m.group(1) not in self.words:
            self.words.append(m.group(1))
        print len(self.words)
        return ""
        #return hex(len(self.words) - 1)[2:]

    def simple(self):
        '''
        simplistic version of obfuscating the script by using the exec() command
        would be slow if the script is long and sophisticated
        '''
        #get rid of the Windows Line Breaks (might be optional)
        s = self.input_str.replace("\r\n", "\n").split("\n")
        for i in xrange(len(s)):
            line = s[i]
            regex_terminal =  re.search(r"([A-Za-z0-9_.]*)", line)
            while regex_terminal != None:
                print line
                line = re.sub(r"([A-Za-z0-9_.]*)", self.add_terminal, line, count=1)
                regex_terminal = re.search(r"([A-Za-z0-9_.]*)", line)
            line = s[i]
            for word in self.words:
                line = line.replace(word, hex(self.words.index(word))[2:])
            s[i] = line

        return "\n".join(s)