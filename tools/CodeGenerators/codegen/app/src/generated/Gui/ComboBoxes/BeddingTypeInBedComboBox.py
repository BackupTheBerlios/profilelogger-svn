from InBedComboBox import *

class BeddingTypeInBedComboBox(InBedComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       BeddingTypeInBedManagementDialog, 
                                       BeddingTypeInBedFinder)
