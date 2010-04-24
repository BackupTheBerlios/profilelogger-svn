from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.Color import Color
from Gui.Dialogs.ColorEditorDialog import ColorEditorDialog

class ColorItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class ColorItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    Color,
                                    ColorItem,
                                    ColorEditorDialog,
                                    ColorFinder)
        self.headerStrings = [self.tr('Colors')]
