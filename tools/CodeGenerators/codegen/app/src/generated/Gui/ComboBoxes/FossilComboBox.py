from InProjectComboBox import *

class FossilComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       FossilManagementDialog, 
                                       FossilFinder)
