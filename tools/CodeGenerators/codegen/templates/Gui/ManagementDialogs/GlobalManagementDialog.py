from ManagementDialog import *

class GlobalManagementDialog(ManagementDialog):
    def __init__(self, parent):
        ManagementDialog.__init__(self, parent, <header>)
        self.addManagementWidget(GlobalTreeView)
        self.addCloseButton()
