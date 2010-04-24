from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.Fossil import Fossil
from Gui.Dialogs.FossilEditorDialog import FossilEditorDialog

class FossilItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class FossilItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    Fossil,
                                    FossilItem,
                                    FossilEditorDialog,
                                    FossilFinder)
        self.headerStrings = [self.tr('Fossils')]
