from InProjectComboBox import *

class GrainSizeTypeComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       GrainSizeTypeManagementDialog, 
                                       GrainSizeTypeFinder)
