import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

# v1

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        self.failIf(app.calc(1) != 1)

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)
        
        lines = output.getvalue().splitlines()

        self.failIf(len(lines) != 100)

        self.failIf(lines[0] != "1")
        self.failIf(lines[1] != "2")
        self.failIf(lines[2] != "Fizz")
        self.failIf(lines[3] != "4")
        self.failIf(lines[4] != "Buzz")
        self.failIf(lines[14] != "FizzBuzz")
        self.failIf(lines[44] != "FizzBuzz")

def main():
    unittest.main()

if __name__ == "__main__":
    main()
