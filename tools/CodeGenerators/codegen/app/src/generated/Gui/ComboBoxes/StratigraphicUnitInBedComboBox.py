from InBedComboBox import *

class StratigraphicUnitInBedComboBox(InBedComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       StratigraphicUnitInBedManagementDialog, 
                                       StratigraphicUnitInBedFinder)
