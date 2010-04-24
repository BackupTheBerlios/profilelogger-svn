from GlobalComboBox import *

class FieldBookComboBox(GlobalComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       FieldBookManagementDialog, 
                                       FieldBookFinder)
