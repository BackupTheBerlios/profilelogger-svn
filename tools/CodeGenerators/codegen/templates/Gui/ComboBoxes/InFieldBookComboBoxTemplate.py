from InFieldBookComboBox import *

class <class_name>ComboBox(InFieldBookComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       <class_name>ManagementDialog, 
                                       <class_name>Finder)
