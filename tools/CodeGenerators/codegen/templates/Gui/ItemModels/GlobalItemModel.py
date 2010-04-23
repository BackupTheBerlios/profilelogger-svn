from ManagementItemModel import ManagementItemModel

from PyQt4.QtGui import *

class GlobalItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class GlobalItemModel(ManagementItemModel):
    def __init__(self, parent):
        ManagementItemModel.__init__(self, parent,
                                     Global,
                                     GlobalItem,
                                     GlobalEditorDialog,
                                     GlobalFinder)
        self.headerStrings = []
