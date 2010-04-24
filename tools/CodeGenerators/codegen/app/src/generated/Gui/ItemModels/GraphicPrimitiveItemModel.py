from ManagementItemModel import ManagementItemModel

from PyQt4.QtGui import *

from Logic.Model.GraphicPrimitive import GraphicPrimitive
from Gui.Dialogs.GraphicPrimitiveEditorDialog import GraphicPrimitiveEditorDialog
from ManagmentItemModel import *

class GraphicPrimitiveItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class GraphicPrimitiveItemModel(ManagementItemModel):
    def __init__(self, parent):
        ManagementItemModel.__init__(self, parent,
                                     GraphicPrimitive,
                                     GraphicPrimitiveItem,
                                     GraphicPrimitiveEditorDialog,
                                     GraphicPrimitiveFinder)
        self.headerStrings = [self.tr('Graphic Primitives')]
