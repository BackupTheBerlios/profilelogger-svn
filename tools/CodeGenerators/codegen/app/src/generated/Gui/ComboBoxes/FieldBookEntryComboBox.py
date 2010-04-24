from InFieldBookComboBox import *

class FieldBookEntryComboBox(InFieldBookComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       FieldBookEntryManagementDialog, 
                                       FieldBookEntryFinder)
