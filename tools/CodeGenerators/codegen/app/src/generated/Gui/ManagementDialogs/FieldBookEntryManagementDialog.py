from InFieldBookManagementDialog import *

from Gui.ItemModels.FieldBookEntryItemModel import *
from Gui.ItemViews.FieldBookEntryItemView import *

class FieldBookEntryManagementDialog(InFieldBookManagementDialog):
    def __init__(self, parent, fieldBook, 'Field Book Entry'):
        InFieldBookManagementDialog.__init__(self, parent, fieldBook, 'Field Book Entry')
        self.addManagementWidget(FieldBookEntryItemView)
        self.addCloseButton()
