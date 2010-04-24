from InProjectComboBox import *

class CustomSymbolComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       CustomSymbolManagementDialog, 
                                       CustomSymbolFinder)
