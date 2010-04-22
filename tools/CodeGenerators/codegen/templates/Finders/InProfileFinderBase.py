"""
Boilderplate comment.
"""

from Finder import *

from Model.InProfile import *

class InProfileFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def doFindAllInProfile(self, dataClass, orderCol, profile):
        if profile is None:
            return None
        return self.getSession().query(dataClass).filter(dataClass.profile == profile).all()
