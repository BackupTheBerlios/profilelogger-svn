from ManagementTreeView import ManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.GraphicPrimitiveItemModel import *

class GraphicPrimitiveItemView(ManagementTreeView):
    def __init__(self, parent):
        ManagementTreeView.__init__(self, parent)
        self.configureModel(GraphicPrimitiveItemModel(self))
