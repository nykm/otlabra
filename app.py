#!/usr/bin/python
import sys

# Implementation of FizzBuzz v2.00

# Version 1: if number is divisible by 3, print Fizz
#            if number is divisible by 5, print Buzz
#            if both, print FizzBuzz
#            else print number

# Version 2: if number is prime, print "<number> is a prime" instead
#            Take one argument,  and count up to it

class FizzBuzz():
    def __init__(self):
        pass

    # Run from 1 to "end". Maybe. Test fails for some reason
    def run(self, end, out=sys.stdout):
        for i in range(1, end + 1):
            print >> out, self.calcv2(i)

    # Seems to give correct values.
    def calcv2(self, i):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime and i > 1:
            return "<%d> is a prime" % i
        else:
            return self.calcv1(i)
     
    def calcv1(self, i):
        imod3 = i % 3
        imod5 = i % 5
        if imod3 == 0 and imod5 == 0:
            return "FizzBuzz"
        if imod3 == 0:
            return "Fizz"
        if imod5 == 0:
            return "Buzz"
        return i

if __name__ == "__main__":
    app = FizzBuzz()
    app.run(100)
