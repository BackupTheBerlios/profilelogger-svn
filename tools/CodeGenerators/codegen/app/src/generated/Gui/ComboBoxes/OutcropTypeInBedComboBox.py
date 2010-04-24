from InBedComboBox import *

class OutcropTypeInBedComboBox(InBedComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       OutcropTypeInBedManagementDialog, 
                                       OutcropTypeInBedFinder)
