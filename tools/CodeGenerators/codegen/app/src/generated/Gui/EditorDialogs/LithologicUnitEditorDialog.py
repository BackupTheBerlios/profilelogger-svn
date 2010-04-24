from Gui.Dialogs.EditorDialog import *

from Logic.Model.LithologicUnit import *

class LithologicUnitEditorDialog(EditorDialog):
    def __init__(self, parent, entity):
        EditorDialog.__init__(self, parent, entity)
