import unittest
import pyobf
import sys
from cStringIO import StringIO

class PyObfSpec(unittest.TestCase):
    def runCode(self, code):
        old = sys.stdout
        redirected_output = sys.stdout = StringIO()
        exec(code)
        sys.stdout = old
        return redirected_output.getvalue()

    def setUp(self):
        pass

    def test_assignment(self):
        string = "print '123'\nprint '456'"
        obf = pyobf.Obfuscator(string)
        self.assertEqual(obf.simple(), "0 \\'1\\'\\n0 \\'2\\'")

    def test_indent(self):
        string = "def main():\n\tprint 'hi'"
        obf = pyobf.Obfuscator(string)
        self.assertEqual(obf.simple(), "0 1():\\n\\t2 \\'3\\'")

    def test_indent_space(self):
        string = "def main():\n    print 'hi'"
        obf = pyobf.Obfuscator(string)
        self.assertEqual(obf.simple(), "0 1():\\n\\t2 \\'3\\'")

    def test_build_simple(self):
        string = "print 'hello world'"
        obf = pyobf.Obfuscator(string)
        self.assertEqual(obf.build_simple(), 
            """exec('''import re
exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),"0 \\'1 2\\'"))(lambda a,b:b[int("0x"+a.group(1),16)],"print|hello|world".split("|")))''')""")

    def tearDown(self):
        pass

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(PyObfSpec)
    unittest.TextTestRunner(verbosity=2).run(suite)
