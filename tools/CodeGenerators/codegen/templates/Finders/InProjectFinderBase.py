"""
Boilderplate comment.
"""

from Finder import *

from Model.InProject import *

class InProjectFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def doFindAllInProject(self, dataClass, orderCol, project):
        if project is None:
            return None
        return self.getSession().query(dataClass).filter(dataClass.project == project).all()
