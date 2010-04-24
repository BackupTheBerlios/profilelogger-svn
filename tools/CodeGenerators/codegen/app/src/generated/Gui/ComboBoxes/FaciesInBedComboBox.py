from InBedComboBox import *

class FaciesInBedComboBox(InBedComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       FaciesInBedManagementDialog, 
                                       FaciesInBedFinder)
