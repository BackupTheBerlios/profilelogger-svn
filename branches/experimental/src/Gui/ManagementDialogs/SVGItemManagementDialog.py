from ManagementDialog import *

from Gui.ItemModels.SVGItemModel import *
from Gui.ItemViews.SVGItemView import *

class SVGItemManagementDialog(ManagementDialog):
    def __init__(self, parent):
        ManagementDialog.__init__(self, parent)
        self.addManagementWidget(SVGItemView, SVGItemModel)
        self.addCloseButton()
