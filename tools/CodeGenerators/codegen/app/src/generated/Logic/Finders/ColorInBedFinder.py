"""
Boilderplate comment.
"""

from InBedFinderBase import *

from Model.ColorInBed import *

class ColorInBedFinder(InBedFinderBase):
    def __init__(self, parent):
        InBedFinderBase.__init__(self, parent)
    def findAll(self, bed):
        if bed is None:
            return None
        return self.doFindAllInBed(ColorInBed, bed)
