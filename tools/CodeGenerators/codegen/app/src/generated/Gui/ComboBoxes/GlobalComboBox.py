from DataSelectionComboBox import *

class GlobalComboBox(DataSelectionComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, parent, managementDialogClass, finderClass)
