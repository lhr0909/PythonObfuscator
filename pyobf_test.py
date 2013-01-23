import unittest
import pyobf

class PyObfSpec(unittest.TestCase):
    def setUp(self):
        pass

    def test_assignment(self):
        string = "print 123"
        obf = pyobf.Obfuscator(string)
        self.assertEqual(obf.simple(), "0 1")

    def tearDown(self):
        pass

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(PyObfSpec)
    unittest.TextTestRunner(verbosity=2).run(suite)