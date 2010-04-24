from InProjectComboBox import *

class GrainSizeComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       GrainSizeManagementDialog, 
                                       GrainSizeFinder)
