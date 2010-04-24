"""
Boilderplate comment.
"""

from InFieldBookFinderBase import *

from Model.FieldBookEntry import *

class FieldBookEntryFinder(InFieldBookFinderBase):
    def __init__(self, parent):
        InFieldBookFinderBase.__init__(self, parent)
    def findAll(self, fieldBook):
        if fieldBook is None:
            return None
        return self.doFindAllInFieldBook(FieldBookEntry, fieldBook)
