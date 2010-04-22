"""
Boilderplate comment.
"""

from Finder import *

from Model.InBed import *

class InBedFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def doFindAllInBed(self, dataClass, orderCol, bed):
        if bed is None:
            return None
        return self.getSession().query(dataClass).filter(dataClass.bed == bed).all()
