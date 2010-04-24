"""
Boilderplate comment.
"""

from InBedFinderBase import *

from Model.FaciesInBed import *

class FaciesInBedFinder(InBedFinderBase):
    def __init__(self, parent):
        InBedFinderBase.__init__(self, parent)
    def findAll(self, bed):
        if bed is None:
            return None
        return self.doFindAllInBed(FaciesInBed, bed)
