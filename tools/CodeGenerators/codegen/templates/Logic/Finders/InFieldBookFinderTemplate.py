"""
Boilderplate comment.
"""

from InFieldBookFinderBase import *

from Model.<class_name> import *

class <class_name>Finder(InFieldBookFinderBase):
    def __init__(self, parent):
        InFieldBookFinderBase.__init__(self, parent)
    def findAll(self, fieldBook):
        if fieldBook is None:
            return None
        return self.doFindAllInFieldBook(<class_name>, fieldBook)
