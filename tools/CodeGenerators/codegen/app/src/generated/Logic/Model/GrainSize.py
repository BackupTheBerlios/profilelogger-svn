"""
Boilerplate comment
"""

from Entity import *


class GrainSize(Entity):
    def __init__(self, id=None, name='new item', description='', project=None, grainSizeType=None, graphicPrimitive=None, percentFromMax=0):
        Entity.__init__(self)
        self.id = id
        self.name = name
        self.description = description
        self.project = project
        self.grainSizeType = grainSizeType
        self.graphicPrimitive = graphicPrimitive
        self.percentFromMax = percentFromMax
