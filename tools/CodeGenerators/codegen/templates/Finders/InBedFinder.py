"""
Boilderplate comment.
"""

from InBedFinderBase import *

from Model.<class_name> import *

class <class_name>Finder(InBedFinderBase):
    def __init__(self, parent):
        InBedFinderBase.__init__(self, parent)
    def findAll(self, bed):
        if bed is None:
            return None
        return self.doFindAllInBed(<class_name>, bed)
