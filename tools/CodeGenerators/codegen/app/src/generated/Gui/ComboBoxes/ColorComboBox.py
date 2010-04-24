from InProjectComboBox import *

class ColorComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       ColorManagementDialog, 
                                       ColorFinder)
