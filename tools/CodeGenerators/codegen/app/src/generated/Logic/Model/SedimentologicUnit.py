"""
Boilerplate comment
"""

from Entity import *


class SedimentologicUnit(Entity):
    def __init__(self, id=None, name='new item', description='', project=None, sedimentologicUnitType=None, graphicPrimitive=None):
        Entity.__init__(self)
        self.id = id
        self.name = name
        self.description = description
        self.project = project
        self.sedimentologicUnitType = sedimentologicUnitType
        self.graphicPrimitive = graphicPrimitive
