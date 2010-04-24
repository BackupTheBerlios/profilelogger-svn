from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.Facies import Facies
from Gui.Dialogs.FaciesEditorDialog import FaciesEditorDialog

class FaciesItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class FaciesItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    Facies,
                                    FaciesItem,
                                    FaciesEditorDialog,
                                    FaciesFinder)
        self.headerStrings = [self.tr('Facies')]
