import test

import unittest

class MyTestCase(unittest.TestCase):

  def test_reverse_string(self):
    result=test.reverse_string('hello')
    self.assertTrue('olleh' in result)

  def test_capitalize_string(self):
    result=test.capitalize_string('hello')
    self.assertTrue('Hello' in result)

  def test_is_capitalized(self):
    result=test.is_capitalized('Hello')
    self.assertTrue(result)


if __name__ == '__main__':
  unittest.main()



