"""
Boilerplate comment
"""

from Entity import *


class GraphicPrimitive(Entity):
    def __init__(self, id=None, name='new item', description='', svgData='', originalPath=''):
        Entity.__init__(self)
        self.id = id
        self.name = name
        self.description = description
        self.svgData = svgData
        self.originalPath = originalPath
