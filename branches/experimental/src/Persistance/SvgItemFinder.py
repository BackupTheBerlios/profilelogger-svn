from Finder import *

from Model.SVGItem import *

class SvgItemFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self):
        return self.doFindAll(SVGItem, SVGItem.name)
