from InProjectComboBox import *

class TectonicUnitComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       TectonicUnitManagementDialog, 
                                       TectonicUnitFinder)
