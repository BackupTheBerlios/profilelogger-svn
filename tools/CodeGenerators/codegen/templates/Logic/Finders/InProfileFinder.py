"""
Boilderplate comment.
"""

from InProfileFinderBase import *

from Model.<class_name> import *

class <class_name>Finder(InProfileFinderBase):
    def __init__(self, parent):
        InProfileFinderBase.__init__(self, parent)
    def findAll(self, profile):
        if profile is None:
            return None
        return self.doFindAllInProfile(<class_name>, profile)
