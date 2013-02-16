import unittest
import pyobf
import sys
import re
from cStringIO import StringIO

class PyObfSpec(unittest.TestCase):
    def runCode(self, code):
        old = sys.stdout
        redirected_output = sys.stdout = StringIO()
        exec(code)
        sys.stdout = old
        return redirected_output.getvalue().strip()

    def setUp(self):
        pass

    def test_assignment(self):
        string = "print '123'\nprint '456'"
        obf = pyobf.Obfuscator(string)
        self.assertEqual(obf.simple(), "0 \\'2\\'\\n0 \\'1\\'")

    def test_indent(self):
        string = "def main():\n\tprint 'hi'"
        obf = pyobf.Obfuscator(string)
        self.assertEqual(obf.simple(), "3 2():\\n\\t1 \\'0\\'")

    def test_indent_space(self):
        string = "def main():\n    print 'hi'"
        obf = pyobf.Obfuscator(string)
        self.assertEqual(obf.simple(), "3 2():\\n\\t1 \\'0\\'")

    def test_build_simple(self):
        string = "print 'hello world'"
        obf = pyobf.Obfuscator(string)
        self.assertEqual(self.runCode(obf.build_simple()), "hello world")

    def tearDown(self):
        pass

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(PyObfSpec)
    unittest.TextTestRunner(verbosity=2).run(suite)
