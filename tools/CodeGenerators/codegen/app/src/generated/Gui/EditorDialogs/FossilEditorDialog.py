from Gui.Dialogs.EditorDialog import *

from Logic.Model.Fossil import *

class FossilEditorDialog(EditorDialog):
    def __init__(self, parent, entity):
        EditorDialog.__init__(self, parent, entity)
