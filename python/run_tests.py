import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))

def get_test_suite(test_modules):
  suite = unittest.TestSuite()
  for t in test_modules:
      try:
          # If the module defines a suite() function, call it to get the suite.
          mod = __import__(t, globals(), locals(), ['suite'])
          suitefn = getattr(mod, 'suite')
          suite.addTest(suitefn())
      except (ImportError, AttributeError):
          # else, just load all the test cases from the module.
          suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))
  return suite

if __name__ == "__main__":
  test_modules = ['tests.collection.test_deque',
                  'tests.crypto.test_ciphers']
  suite = get_test_suite(test_modules)
  unittest.TextTestRunner().run(suite)
