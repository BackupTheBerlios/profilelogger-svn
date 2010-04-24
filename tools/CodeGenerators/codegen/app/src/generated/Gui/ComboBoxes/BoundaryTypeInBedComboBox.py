from InBedComboBox import *

class BoundaryTypeInBedComboBox(InBedComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       BoundaryTypeInBedManagementDialog, 
                                       BoundaryTypeInBedFinder)
