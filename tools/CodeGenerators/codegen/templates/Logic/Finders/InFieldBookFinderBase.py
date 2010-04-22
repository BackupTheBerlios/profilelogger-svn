"""
Boilderplate comment.
"""

from Finder import *

from Model.InFieldBook import *

class InFieldBookFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def doFindAllInFieldBook(self, dataClass, orderCol, fieldBook):
        if fieldBook is None:
            return None
        return self.getSession().query(dataClass).filter(dataClass.fieldBook == fieldBook).all()
