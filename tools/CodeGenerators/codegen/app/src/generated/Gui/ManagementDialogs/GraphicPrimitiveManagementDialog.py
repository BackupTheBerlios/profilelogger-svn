from GlobalManagementDialog import *

from Gui.ItemModels.GraphicPrimitiveItemModel import *
from Gui.TreeViews.GraphicPrimitiveTreeView import *

class GraphicPrimitiveManagementDialog(GlobalManagementDialog):
    def __init__(self, parent):
        GlobalManagementDialog.__init__(self, parent, 'Graphic Primitives')
        self.addManagementWidget(GraphicPrimitiveTreeView)
        self.addCloseButton()
