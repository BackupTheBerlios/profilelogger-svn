from InBedComboBox import *

class TectonicUnitInBedComboBox(InBedComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       TectonicUnitInBedManagementDialog, 
                                       TectonicUnitInBedFinder)
