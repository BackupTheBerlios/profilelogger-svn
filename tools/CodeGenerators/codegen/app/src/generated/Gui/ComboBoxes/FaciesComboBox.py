from InProjectComboBox import *

class FaciesComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       FaciesManagementDialog, 
                                       FaciesFinder)
