from InProjectComboBox import *

class BoundaryTypeComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       BoundaryTypeManagementDialog, 
                                       BoundaryTypeFinder)
