import re
import base64

class Obfuscator:
    input_str = ""
    words = dict()
    word_list = []
    output_lines = []

    def __init__(self, s):
        self.input_str = s
        self.words = dict()
        self.word_list = []
        self.output_lines = []

    def add_terminal(self, m):
        if m.group(1) not in self.words:
            self.words[m.group(1)] = 1
        else:
            self.words[m.group(1)] += 1
        return ""
        #return hex(len(self.words) - 1)[2:]

    def simple(self):
        '''
        simplistic version of obfuscating the script by using the exec() command
        would be slow if the script is long and sophisticated
        '''
        #get rid of the Windows Line Breaks (might be optional)
        indent_size = 0
        indent_checked = False
        s = self.input_str.replace("\r\n", "\n").split("\n")
        for i in xrange(len(s)):
            #check indentation (convert spaces to tabs)
            line = s[i]
            if line.startswith(" ") and not indent_checked:
                while line.startswith(" "):
                    line = line[1:]
                    indent_size += 1
                indent_checked = True
            if indent_size > 0:
                line = s[i].replace(" " * indent_size, "\t")
            s[i] = line
            #add words
            regex_terminal =  re.search(r"([A-Za-z0-9_]+)", line)
            while regex_terminal != None:
                line = re.sub(r"([A-Za-z0-9_]+)", self.add_terminal, line, count=1)
                regex_terminal = re.search(r"([A-Za-z0-9_]+)", line)


        #sort words by frequencies
        for (key, value) in self.words.items():
            self.words[key] = value * len(key)
        self.word_list = self.words.keys()
        self.word_list.sort(key=self.words.get)
        self.word_list.reverse()

        # put the words to its own slot if the encoding is the same
        last_i = 0
        last_x = 1
        wordLen = len(self.word_list)
        i = 0
        while i < wordLen:
            word = self.word_list[i]

            try:
                x = int("0x" + word, 16)
            except:
                i += 1
                continue

            if wordLen > x and i != x and x != last_x and i != last_i and self.word_list[i].lower() != self.word_list[x].lower():
                #print x, i, self.word_list[x], self.word_list[i]
                temp = self.word_list[i]
                self.word_list[i] = self.word_list[x]
                self.word_list[x] = temp
                #print x, i, self.word_list[x], self.word_list[i]
                last_x = x
                last_i = i
                i = 0
                continue
            i += 1

        #replace words
        for i in xrange(len(s)):
            line = s[i]
            for word in self.word_list:
                line = re.sub(r"\b" + word + r"\b", hex(self.word_list.index(word))[2:], line)
            s[i] = line

        self.output_lines = s[:]
        return "\n".join(s)

    def print_word_list(self):
        for word in self.word_list:
            print hex(self.word_list.index(word)), word

    def build_simple(self):
        '''
        return a string of obfuscated python script
        '''
        obf_str = base64.b64encode(self.simple())
        words_str = "|".join(self.word_list)

        return r"""exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("%s")))(lambda a,b:b[int("0x"+a.group(1),16)],"%s".split("|")))""" % (obf_str, words_str)
