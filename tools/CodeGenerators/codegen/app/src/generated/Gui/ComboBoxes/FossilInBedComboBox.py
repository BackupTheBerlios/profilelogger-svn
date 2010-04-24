from InBedComboBox import *

class FossilInBedComboBox(InBedComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       FossilInBedManagementDialog, 
                                       FossilInBedFinder)
