import re

def subWords(m, words):
    return words[int("0x" + m.group(1), 16)]

words = ['print', "'123'"]
print re.sub(r"([0-9a-f]*)", lambda m: subWords(m, words), "0 1")
