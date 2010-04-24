from InProjectComboBox import *

class LithologicUnitTypeComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       LithologicUnitTypeManagementDialog, 
                                       LithologicUnitTypeFinder)
