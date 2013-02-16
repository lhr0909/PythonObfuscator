'''
import re

def subWords(m, words):
    return words[int("0x" + m.group(1), 16)]

words = ['print', "'123'"]
print re.sub(r"([0-9a-f]*)", lambda m: subWords(m, words), "0 1")
'''


import re

def subFunc(m, words):
    return words[int("0x" + m.group(1), 16)]

def main(pattern, func, string):
    return re.sub(pattern, func, string)

print main(r"([0-9a-f]+)", lambda m:subFunc(m, "a|2|b|0|for|i|in|range|1901|2001|c|1|13|if|4|or|6|9|11|30|elif|29|else|28|31|7|print".split("|")), "0 = 1\\n2 = 3\\n4 5 6 7(8, 9):\\n\\t4 a 6 7(b, c):\\n\\t\\td (a==e)f(a==10)f(a==12)f(a==12):\\n\\t\\t\\t3 = 3 + 13\\n\\t\\t14 a==b:\\n\\t\\t\\td 5 % e==3:\\n\\t\\t\\t\\t3 = 3 + 15\\n\\t\\t\\t16:\\n\\t\\t\\t\\t3 = 3 + 17\\n\\t\\t16:\\n\\t\\t\\t3 = 3 + 18\\n\\t\\td 3 % 19==3:\\n\\t\\t\\t2 = 2 + b\\n1a 2")



'''
import re
print (lambda p, y: (lambda o, b, f: re.sub(o, b, f))(r"([0-9a-f]+)", lambda m:p(m, y), "0 '1'"))(lambda a, b: b[int("0x" + a.group(1), 16)], "print|123".split("|"))
'''

"""
exec('''import re\nexec((lambda p, y: (lambda o, b, f: re.sub(o, b, f))(r"([0-9a-f]+)", lambda m:p(m, y), "0 '1'"))(lambda a, b: b[int("0x" + a.group(1), 16)], "print|123".split("|")))''')
"""