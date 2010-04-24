from InProjectComboBox import *

class LithologyComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       LithologyManagementDialog, 
                                       LithologyFinder)
