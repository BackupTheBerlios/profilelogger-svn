from InProjectComboBox import *

class TectonicUnitTypeComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       TectonicUnitTypeManagementDialog, 
                                       TectonicUnitTypeFinder)
