"""
Boilerplate comment
"""

from Entity import *


class StratigraphicUnit(Entity):
    def __init__(self, id=None, name='new item', description='', project=None, stratigraphicUnitType=None, graphicPrimitive=None):
        Entity.__init__(self)
        self.id = id
        self.name = name
        self.description = description
        self.project = project
        self.stratigraphicUnitType = stratigraphicUnitType
        self.graphicPrimitive = graphicPrimitive
