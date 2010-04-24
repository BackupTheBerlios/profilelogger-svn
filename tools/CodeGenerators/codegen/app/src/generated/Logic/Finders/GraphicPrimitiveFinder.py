"""
Boilderplate comment
"""

from Finder import *

from Model.GraphicPrimitive import *

class GraphicPrimitiveFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self):
        return self.doFindAll(GraphicPrimitive)
