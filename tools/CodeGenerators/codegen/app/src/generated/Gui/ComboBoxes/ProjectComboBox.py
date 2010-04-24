from GlobalComboBox import *

class ProjectComboBox(GlobalComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       ProjectManagementDialog, 
                                       ProjectFinder)
