from InProjectComboBox import *

class SedimentologicUnitComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       SedimentologicUnitManagementDialog, 
                                       SedimentologicUnitFinder)
