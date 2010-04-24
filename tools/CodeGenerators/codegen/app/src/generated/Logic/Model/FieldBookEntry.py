"""
Boilerplate comment
"""

from Entity import *


class FieldBookEntry(Entity):
    def __init__(self, id=None, fieldBook=None):
        Entity.__init__(self)
        self.id = id
        self.fieldBook = fieldBook
