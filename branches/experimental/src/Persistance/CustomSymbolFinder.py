from Finder import *

from Model.CustomSymbol import *

class CustomSymbolFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(CustomSymbol, CustomSymbol.name, project)
