"""
Boilerplate comment
"""

from Entity import *


class Bed(Entity):
    def __init__(self, id=None, position=None, bedNumber=None, profile=None, height=0, heightLenghtUnit=None):
        Entity.__init__(self)
        self.id = id
        self.position = position
        self.bedNumber = bedNumber
        self.profile = profile
        self.height = height
        self.heightLenghtUnit = heightLenghtUnit
