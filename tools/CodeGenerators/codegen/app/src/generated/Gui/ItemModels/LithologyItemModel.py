from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.Lithology import Lithology
from Gui.Dialogs.LithologyEditorDialog import LithologyEditorDialog

class LithologyItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class LithologyItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    Lithology,
                                    LithologyItem,
                                    LithologyEditorDialog,
                                    LithologyFinder)
        self.headerStrings = [self.tr('Lithologies')]
