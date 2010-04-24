from InProjectComboBox import *

class OutcropTypeComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       OutcropTypeManagementDialog, 
                                       OutcropTypeFinder)
