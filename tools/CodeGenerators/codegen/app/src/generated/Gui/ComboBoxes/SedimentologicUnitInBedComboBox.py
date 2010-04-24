from InBedComboBox import *

class SedimentologicUnitInBedComboBox(InBedComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       SedimentologicUnitInBedManagementDialog, 
                                       SedimentologicUnitInBedFinder)
