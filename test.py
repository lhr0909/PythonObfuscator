'''
import re

def subWords(m, words):
    return words[int("0x" + m.group(1), 16)]

words = ['print', "'123'"]
print re.sub(r"([0-9a-f]*)", lambda m: subWords(m, words), "0 1")
'''

'''
import re

def subFunc(m, words):
    return words[int("0x" + m.group(1), 16)]

def main(pattern, func, string):
    return re.sub(pattern, func, string)

print main(r"([0-9a-f]+)", lambda m:subFunc(m, ['print', '123']), '0 "1"')

'''

'''
import re
print (lambda p, y: (lambda o, b, f: re.sub(o, b, f))(r"([0-9a-f]+)", lambda m:p(m, y), "0 '1'"))(lambda a, b: b[int("0x" + a.group(1), 16)], "print|123".split("|"))
'''

exec('''import re\nexec((lambda p, y: (lambda o, b, f: re.sub(o, b, f))(r"([0-9a-f]+)", lambda m:p(m, y), "0 '1'"))(lambda a, b: b[int("0x" + a.group(1), 16)], "print|123".split("|")))''')