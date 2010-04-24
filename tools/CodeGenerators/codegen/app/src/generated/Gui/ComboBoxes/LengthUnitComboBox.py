from GlobalComboBox import *

class LengthUnitComboBox(GlobalComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       LengthUnitManagementDialog, 
                                       LengthUnitFinder)
