"""
Boilerplate comment
"""

from Entity import *


class LithologicUnit(Entity):
    def __init__(self, id=None, name='new item', description='', project=None, lithologicUnitType=None, graphicPrimitive=None):
        Entity.__init__(self)
        self.id = id
        self.name = name
        self.description = description
        self.project = project
        self.lithologicUnitType = lithologicUnitType
        self.graphicPrimitive = graphicPrimitive
