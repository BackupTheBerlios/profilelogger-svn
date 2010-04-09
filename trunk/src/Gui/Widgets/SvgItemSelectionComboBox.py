from DataSelectionComboBox import DataSelectionComboBox

from Gui.ManagementDialogs.SVGItemManagementDialog import *
from Persistance.SvgItemFinder import *

class SvgItemSelectionComboBox(DataSelectionComboBox):
    def __init__(self, parent):
        DataSelectionComboBox.__init__(self, parent, 
                                       SVGItemManagementDialog,
                                       SvgItemFinder)
        self.setToolTip(self.tr("SVG Items"))
