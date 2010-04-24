"""
Boilderplate comment.
"""

from InBedFinderBase import *

from Model.TectonicUnitInBed import *

class TectonicUnitInBedFinder(InBedFinderBase):
    def __init__(self, parent):
        InBedFinderBase.__init__(self, parent)
    def findAll(self, bed):
        if bed is None:
            return None
        return self.doFindAllInBed(TectonicUnitInBed, bed)
