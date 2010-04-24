from InProjectComboBox import *

class SedimentologicUnitTypeComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       SedimentologicUnitTypeManagementDialog, 
                                       SedimentologicUnitTypeFinder)
