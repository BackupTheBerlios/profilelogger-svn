"""
Boilderplate comment
"""

from Finder import *

from Model.FieldBook import *

class FieldBookFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self):
        return self.doFindAll(FieldBook)
