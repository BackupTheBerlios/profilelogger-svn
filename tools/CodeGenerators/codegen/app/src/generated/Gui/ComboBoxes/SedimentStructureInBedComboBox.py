from InBedComboBox import *

class SedimentStructureInBedComboBox(InBedComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       SedimentStructureInBedManagementDialog, 
                                       SedimentStructureInBedFinder)
