from InBedComboBox import *

class GrainSizeInBedComboBox(InBedComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       GrainSizeInBedManagementDialog, 
                                       GrainSizeInBedFinder)
