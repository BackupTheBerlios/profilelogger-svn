from InProjectComboBox import *

class SedimentStructureComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       SedimentStructureManagementDialog, 
                                       SedimentStructureFinder)
