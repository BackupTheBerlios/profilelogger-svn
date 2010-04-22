from InProjectFinderBase import *

from Model.<class_name> import *

class <class_name>Finder(InProjectFinderBase):
    def __init__(self, parent):
        InProjectFinderBase.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(<class_name>, project)
