"""
Boilderplate comment.
"""

from InProfileFinderBase import *

from Model.ProfileColumn import *

class ProfileColumnFinder(InProfileFinderBase):
    def __init__(self, parent):
        InProfileFinderBase.__init__(self, parent)
    def findAll(self, profile):
        if profile is None:
            return None
        return self.doFindAllInProfile(ProfileColumn, profile)
