from GlobalComboBox import *

class GraphicPrimitiveComboBox(GlobalComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       GraphicPrimitiveManagementDialog, 
                                       GraphicPrimitiveFinder)
