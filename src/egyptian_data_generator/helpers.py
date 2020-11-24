import numpy
import sys
import datetime

class Helpers:
    @staticmethod
    def replaceSymbolWithNumber(_string):
        res = ''
        for i in range(0, len(_string)): 
            if(_string[i] == '#'):
                res = res + str(Helpers.intBetween(0, 9))
            else:
                res = res + _string[i]
        return res

    @staticmethod
    def intBetween(_start, _end = sys.maxsize):
        return numpy.random.randint(_start, _end)

    @staticmethod
    def oneChoice(_array, _end = sys.maxsize):
        myChoice = numpy.random.choice(_array, 1)
        return myChoice[0]
