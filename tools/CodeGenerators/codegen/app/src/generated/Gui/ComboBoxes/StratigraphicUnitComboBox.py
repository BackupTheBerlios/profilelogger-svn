from InProjectComboBox import *

class StratigraphicUnitComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       StratigraphicUnitManagementDialog, 
                                       StratigraphicUnitFinder)
