from InBedComboBox import *

class CustomSymbolInBedComboBox(InBedComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       CustomSymbolInBedManagementDialog, 
                                       CustomSymbolInBedFinder)
