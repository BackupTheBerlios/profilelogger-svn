"""
Boilderplate comment.
"""

from InProfileFinderBase import *

from Model.ProfileColumnInProfile import *

class ProfileColumnInProfileFinder(InProfileFinderBase):
    def __init__(self, parent):
        InProfileFinderBase.__init__(self, parent)
    def findAll(self, profile):
        if profile is None:
            return None
        return self.doFindAllInProfile(ProfileColumnInProfile, profile)
