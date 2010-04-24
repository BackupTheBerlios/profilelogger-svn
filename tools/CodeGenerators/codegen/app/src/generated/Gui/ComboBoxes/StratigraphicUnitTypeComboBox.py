from InProjectComboBox import *

class StratigraphicUnitTypeComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       StratigraphicUnitTypeManagementDialog, 
                                       StratigraphicUnitTypeFinder)
