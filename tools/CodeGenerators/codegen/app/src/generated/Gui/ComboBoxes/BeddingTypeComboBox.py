from InProjectComboBox import *

class BeddingTypeComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       BeddingTypeManagementDialog, 
                                       BeddingTypeFinder)
