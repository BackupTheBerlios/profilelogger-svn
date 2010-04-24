"""
Boilerplate comment
"""

from Entity import *


class ProfileColumnInProfile(Entity):
    def __init__(self, profile=None, profileColumn=None, position=0):
        Entity.__init__(self)
        self.profile = profile
        self.profileColumn = profileColumn
        self.position = position
