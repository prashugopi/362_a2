import random
import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def testOne(self):
        password = ''
        self.assertFalse(check_pwd(password))

    def testTwo(self):
        password = 'ABCDEFGHIJ'
        self.assertFalse(check_pwd(password))

    def testThree(self):
        password = 'abcdefghij'
        self.assertFalse(check_pwd(password))

    def testFour(self):
        password = 'abcdEFGHIJ'
        self.assertFalse(check_pwd(password))

    def testFive(self):
        password = 'abcdEFGHIJ1'
        self.assertFalse(check_pwd(password))

if __name__ == '__main__':
    unittest.main()